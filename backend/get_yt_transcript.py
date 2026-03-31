#!/usr/bin/env python3
import sys
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def get_transcript(video_id):
    try:
        # Try English first, then any available language
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        except Exception:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        text = ' '.join([entry['text'] for entry in transcript_list])
        print(text)
        sys.exit(0)
    except TranscriptsDisabled:
        print("ERROR: Transcripts are disabled for this video.", file=sys.stderr)
        sys.exit(1)
    except NoTranscriptFound:
        print("ERROR: No transcript found for this video.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_yt_transcript.py VIDEO_ID", file=sys.stderr)
        sys.exit(1)
    get_transcript(sys.argv[1])
