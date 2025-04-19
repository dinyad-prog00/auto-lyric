## 🔗 Useful Links

-  [WhisperX (Word-level transcription)](https://github.com/m-bain/whisperx)
-  [Whisper-small on Hugging Face](https://huggingface.co/openai/whisper-small)
-  [OpenAI Whisper (Base model)](https://github.com/openai/whisper)
-  [FFmpeg – Video processing toolkit](https://ffmpeg.org/download.html)
-  [FFmpeg Subtitle Filters Documentation](https://ffmpeg.org/ffmpeg-filters.html#subtitles-1)
-  [ffsubsync – Sync subtitles to speech](https://github.com/smacke/ffsubsync)
-  [ASS Subtitle Format Specification](http://www.tcax.org/docs/ass-specs.htm)
  
## 📦 Requirements

- Python 3.9+
- `ffmpeg` (ask chatpgt how to install on ubunutu)
- WhisperX  (pip install whisperx)


📄 Example Usage

1. Transcribe video using WhisperX

whisperx input.mp4 --model medium --output_format json --compute_type float32 --output_dir output/

2. Add subtitle to video

ffmpeg -i input.mp4 -vf "subtitles=output/input.srt" output/video_with_subtitles.mp4


First example i show yu

[For Visualize & play word-level time-aligned lyrics in LRC format](https://github.com/mikezzb/lrc-player)