# LEGO Space Roller Coaster — frame snapshots

Source: JK Brickworks, "LIVE • Building and Trying to Motorize the LEGO Space
Roller Coaster" — https://www.youtube.com/live/ArJaMXTIXgY (2:44:16 total).

181 stills covering **1:55:00 → 2:25:00**, one every 10 seconds.
Filenames encode the timestamp: `lego_HH-MM-SS.jpg`.

## Caveat on resolution

These are 320×180. The video's own streams were not downloadable from the
environment these were pulled in (Google returned HTTP 403 on every
`googlevideo.com` media request and 429 on youtube.com; the remaining
non-SABR format was also blocked). The frames therefore come from YouTube's
storyboard track (`storyboard3_L3`), which happens to be sampled at exactly
10 s intervals — the requested cadence — but only at thumbnail resolution.

To regenerate at full resolution from a machine that can reach YouTube
normally:

```sh
yt-dlp -f 'bv*[height<=1080]' -o lego.mp4 https://www.youtube.com/live/ArJaMXTIXgY
ffmpeg -ss 6900 -i lego.mp4 -t 1800 -vf fps=1/10 -q:v 2 lego_%03d.jpg
```

## Transcript

- `transcript.srt` — full 2:44:16, 1768 cue lines, 15 012 words.
- `snapshots.csv` — `seconds, timestamp, image, transcript`, one row per frame.
- `snapshots.md` — the same thing rendered: each frame followed by what was
  said from that frame until the next, with a deep link into the video.

Text under a frame at time *t* covers the window **[t, t+10)** — i.e. what
was said starting at that frame. 172 of the 181 frames have speech.

### Where the text comes from

This is **YouTube's own auto-caption track** (`en-orig`, json3, word-level
timings), not a fresh transcription. The audio stream is behind the same
403 block described above, so there was nothing local to run an ASR model
over. Practical consequences: no punctuation or speaker labels, occasional
ASR errors on LEGO-specific vocabulary, and accuracy is whatever YouTube's
model produced.

To re-transcribe properly from a machine that can reach YouTube:

```sh
yt-dlp -x --audio-format wav -o lego.wav https://www.youtube.com/live/ArJaMXTIXgY
whisper lego.wav --model medium.en --output_format srt
```
