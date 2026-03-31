#!/usr/bin/env python3
import sys
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        try:
            # Try fetching English first
            fetched = api.fetch(video_id, languages=['en'])
        except Exception:
            # Fallback to any available language
            fetched = api.fetch(video_id)
        # Support both old list-of-dicts and new FetchedTranscript object
        if hasattr(fetched, 'snippets'):
            text = ' '.join([s.text for s in fetched.snippets])
        else:
            text = ' '.join([entry['text'] for entry in fetched])
        print(text)
        sys.exit(0)
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_yt_transcript.py VIDEO_ID", file=sys.stderr)
        sys.exit(1)
    get_transcript(sys.argv[1])
