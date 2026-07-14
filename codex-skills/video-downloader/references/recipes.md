# Download Recipes

Use these recipes only for media the user is authorized to download. Prefer `scripts/download_media.py`; use direct commands for inspection or special cases.

## Inspect Before Downloading

```bash
yt-dlp --dump-single-json --no-playlist "URL"
yt-dlp --list-formats --no-playlist "URL"
```

## Video

Best MP4-compatible streams up to 1080p:

```bash
yt-dlp --no-playlist --no-overwrites \
  -f "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/bv*[height<=1080]+ba/b[height<=1080]" \
  --merge-output-format mp4 \
  -o "%(title)s-%(id)s.%(ext)s" "URL"
```

## Audio

```bash
yt-dlp --no-playlist -x --audio-format m4a \
  -o "%(title)s-%(id)s.%(ext)s" "URL"
```

## Subtitles And Metadata

```bash
yt-dlp --no-playlist --skip-download \
  --write-subs --write-auto-subs --sub-langs "all,-live_chat" --sub-format "srt/best" \
  --write-info-json --write-description --write-thumbnail \
  -o "%(title)s-%(id)s.%(ext)s" "URL"
```

Prefer manually created subtitles over automatic subtitles when both exist. Keep timestamps intact for later citation and content distillation.

## Playlist

Inspect playlist count before downloading. Then use a stable indexed path:

```bash
yt-dlp --yes-playlist --no-overwrites \
  -o "%(playlist_title)s/%(playlist_index)03d-%(title)s-%(id)s.%(ext)s" \
  "PLAYLIST_URL"
```

## Verification

```bash
ffprobe -v error -show_entries format=filename,duration,size \
  -show_entries stream=codec_type,codec_name,width,height \
  -of json "OUTPUT_FILE"
```

Confirm that duration, dimensions, codecs, and size match the request. For batches, report failed items separately rather than claiming the entire batch succeeded.
