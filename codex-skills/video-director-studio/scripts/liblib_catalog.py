#!/usr/bin/env python3
"""Fetch and normalize public LibTV Skill catalog metadata.

The endpoint is used by the public website but is not documented as a stable API.
This script intentionally fetches only unauthenticated catalog metadata.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


CATALOG_URL = "https://www.liblib.tv/skill"
FEED_URL = "https://api.liblib.tv/api/community/skill/template/feed/stream"


TAG_RULES = [
    ("production-module", r"分镜|选角|剧本|画幅|风格提取|诊断|空镜|微表情|预演|世界观|关系"),
    ("commercial", r"TVC|广告|产品|带货|种草|品牌|营销|海报|模特|穿搭|护肤|美妆"),
    ("short-drama", r"短剧|漫剧|甜宠|男频|女频|狼人|吸血鬼"),
    ("music-video", r"MV|音乐|词曲|歌曲|偶像"),
    ("creator-ugc", r"口播|自媒体|教学|测评|脱口秀|Vlog|烹饪|博主|达人"),
    ("animation-game", r"动画|动漫|游戏|玩偶|剪纸|浮世绘|低多边形|魔法少女|手办|毛毡"),
    ("documentary-travel", r"纪录|旅拍|旅行|人文|老城|生活感"),
    ("cinematic", r"电影|导演|影视|喜剧|片头|特效|美学"),
]


def compact(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def infer_pattern_tags(item: dict[str, Any]) -> list[str]:
    text = " ".join(
        compact(item.get(key))
        for key in ("name", "description", "useScenario", "inputType", "outputContent")
    )
    matches = [tag for tag, pattern in TAG_RULES if re.search(pattern, text, re.IGNORECASE)]
    return matches or ["cinematic"]


def fetch_page(page: int, page_size: int, timeout: float) -> dict[str, Any]:
    payload = json.dumps({"page": page, "pageSize": page_size}).encode("utf-8")
    request = Request(
        FEED_URL,
        data=payload,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Origin": "https://www.liblib.tv",
            "Referer": CATALOG_URL,
            "X-Language": "zh",
            "Webid": "video-director-studio-public-metadata",
            "User-Agent": "video-director-studio/1.0 (+public metadata research)",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        body = json.loads(response.read().decode("utf-8"))
    if body.get("code") != 0:
        raise RuntimeError(f"catalog returned code={body.get('code')}: {body.get('msg', '')}")
    return body.get("data") or {}


def normalize_item(item: dict[str, Any]) -> dict[str, Any]:
    tags = item.get("tags") or []
    category = compact(tags[0].get("tagLabel")) if tags and isinstance(tags[0], dict) else "Uncategorized"
    return {
        "template_uuid": compact(item.get("templateUuid")),
        "skill_key": compact(item.get("skillKey")),
        "name": compact(item.get("name")),
        "category": category,
        "description": compact(item.get("description")),
        "use_scenario": compact(item.get("useScenario")),
        "input_type": compact(item.get("inputType")),
        "output_content": compact(item.get("outputContent")),
        "version": compact(item.get("version")),
        "published_at": compact(item.get("publishAt")),
        "markdown_public": bool(item.get("showMarkdown")),
        "pattern_tags": infer_pattern_tags(item),
    }


def fetch_catalog(page_size: int, timeout: float) -> dict[str, Any]:
    raw_items: list[dict[str, Any]] = []
    expected_total: int | None = None
    page = 1
    while page <= 20:
        data = fetch_page(page, page_size, timeout)
        items = data.get("list") or []
        if not isinstance(items, list):
            raise RuntimeError("catalog response data.list is not an array")
        raw_items.extend(item for item in items if isinstance(item, dict))
        if isinstance(data.get("total"), int):
            expected_total = data["total"]
        has_more = bool(data.get("hasMore"))
        if not has_more or not items or (expected_total is not None and len(raw_items) >= expected_total):
            break
        page += 1

    items = [normalize_item(item) for item in raw_items]
    categories = Counter(item["category"] for item in items)
    pattern_tags = Counter(tag for item in items for tag in item["pattern_tags"])
    return {
        "source": CATALOG_URL,
        "feed": FEED_URL,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "stability": "undocumented-public-web-endpoint",
        "expected_total": expected_total,
        "returned_total": len(items),
        "categories": dict(sorted(categories.items())),
        "pattern_tags": dict(sorted(pattern_tags.items())),
        "items": items,
    }


def md_escape(value: Any) -> str:
    return compact(value).replace("|", "\\|")


def to_markdown(catalog: dict[str, Any]) -> str:
    lines = [
        "# LibTV Public Skill Catalog",
        "",
        f"- Source: {catalog['source']}",
        f"- Fetched at: {catalog['fetched_at']}",
        f"- Returned: {catalog['returned_total']} / expected {catalog.get('expected_total')}",
        "- Scope: public metadata only; the feed is undocumented and may change.",
        "",
        "## Categories",
        "",
        "| Category | Count |",
        "| --- | ---: |",
    ]
    for category, count in catalog["categories"].items():
        lines.append(f"| {md_escape(category)} | {count} |")
    lines.extend(
        [
            "",
            "## Items",
            "",
            "| Category | Name | Version | Published | Pattern tags | Template UUID |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in catalog["items"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_escape(item["category"]),
                    md_escape(item["name"]),
                    md_escape(item["version"]),
                    md_escape(item["published_at"]),
                    md_escape(", ".join(item["pattern_tags"])),
                    md_escape(item["template_uuid"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--output", type=Path, help="Write to this file instead of stdout")
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--timeout", type=float, default=30.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not 1 <= args.page_size <= 100:
        print("error: --page-size must be between 1 and 100", file=sys.stderr)
        return 2
    try:
        catalog = fetch_catalog(args.page_size, args.timeout)
    except (HTTPError, URLError, TimeoutError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"error: could not fetch public LibTV catalog metadata: {exc}", file=sys.stderr)
        return 2

    rendered = (
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
        if args.format == "json"
        else to_markdown(catalog)
    )
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
