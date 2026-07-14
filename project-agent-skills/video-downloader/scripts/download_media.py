#!/usr/bin/env python3
"""Build and run conservative yt-dlp download commands."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download permitted online media with yt-dlp."
    )
    parser.add_argument("urls", nargs="+", help="HTTP(S) media or playlist URL")
    parser.add_argument("--output-dir", default="downloads")
    parser.add_argument("--quality", type=int, choices=(480, 720, 1080, 1440, 2160))
    parser.add_argument("--format", choices=("mp4", "webm", "best"), default="mp4")
    parser.add_argument("--audio-only", action="store_true")
    parser.add_argument("--audio-format", choices=("m4a", "mp3", "opus", "wav"), default="m4a")
    parser.add_argument("--playlist", action="store_true")
    parser.add_argument("--subtitles", action="store_true")
    parser.add_argument("--subtitle-langs", default="all,-live_chat")
    parser.add_argument("--metadata", action="store_true")
    parser.add_argument("--thumbnail", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Print command without running it")
    return parser.parse_args()


def validate_urls(urls: list[str]) -> None:
    for url in urls:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError(f"Only HTTP(S) URLs are accepted: {url}")


def format_selector(args: argparse.Namespace) -> str:
    height = f"[height<={args.quality}]" if args.quality else ""
    if args.format == "best":
        return f"bv*{height}+ba/b{height}"
    ext = args.format
    return (
        f"bv*{height}[ext={ext}]+ba[ext=m4a]/"
        f"bv*{height}+ba/b{height}"
    )


def build_command(args: argparse.Namespace) -> list[str]:
    command = ["yt-dlp", "--ignore-config", "--newline", "--restrict-filenames"]
    command.append("--yes-playlist" if args.playlist else "--no-playlist")
    command.extend(["--no-overwrites", "--continue", "--part"])

    output_dir = Path(args.output_dir).expanduser().resolve()
    if args.playlist:
        template = output_dir / "%(playlist_title)s" / "%(playlist_index)03d-%(title)s-%(id)s.%(ext)s"
    else:
        template = output_dir / "%(title)s-%(id)s.%(ext)s"
    command.extend(["--output", str(template)])

    if args.audio_only:
        command.extend(["--extract-audio", "--audio-format", args.audio_format])
    else:
        command.extend(["--format", format_selector(args)])
        if args.format in {"mp4", "webm"}:
            command.extend(["--merge-output-format", args.format])

    if args.subtitles:
        command.extend(
            [
                "--write-subs",
                "--write-auto-subs",
                "--sub-langs",
                args.subtitle_langs,
                "--sub-format",
                "srt/best",
            ]
        )
    if args.metadata:
        command.extend(["--write-info-json", "--write-description"])
    if args.thumbnail:
        command.append("--write-thumbnail")

    command.extend(args.urls)
    return command


def main() -> int:
    args = parse_args()
    try:
        validate_urls(args.urls)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if not shutil.which("yt-dlp"):
        print("error: yt-dlp is not installed or not on PATH", file=sys.stderr)
        return 127
    if (args.audio_only or args.format != "best") and not shutil.which("ffmpeg"):
        print("error: ffmpeg is required for extraction or merging", file=sys.stderr)
        return 127

    command = build_command(args)
    if args.dry_run:
        print(json.dumps(command, ensure_ascii=True, indent=2))
        return 0

    Path(args.output_dir).expanduser().mkdir(parents=True, exist_ok=True)
    return subprocess.run(command, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
