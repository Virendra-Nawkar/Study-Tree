#!/usr/bin/env python3
import sys
import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig, GenericProxyConfig

def get_transcript(video_id):
    try:
        # Build proxy config from environment variables if available
        proxy_user = os.environ.get('PROXY_USERNAME')
        proxy_pass = os.environ.get('PROXY_PASSWORD')
        proxy_host = os.environ.get('PROXY_HOST')
        proxy_port = os.environ.get('PROXY_PORT')

        if proxy_user and proxy_pass:
            print(f"Using Webshare proxy", file=sys.stderr)
            proxy_config = WebshareProxyConfig(
                proxy_username=proxy_user,
                proxy_password=proxy_pass
            )
            api = YouTubeTranscriptApi(proxy_config=proxy_config)
        else:
            api = YouTubeTranscriptApi()

        import time
        try:
            fetched = api.fetch(video_id, languages=['en'])
        except Exception:
            time.sleep(3)
            fetched = api.fetch(video_id)

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
