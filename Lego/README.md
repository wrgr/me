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
