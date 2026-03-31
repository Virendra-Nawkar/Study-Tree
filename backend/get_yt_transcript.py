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

        if proxy_host and proxy_port and proxy_user and proxy_pass:
            print(f"Using proxy: {proxy_host}:{proxy_port}", file=sys.stderr)
            proxy_config = GenericProxyConfig(
                http_url=f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}",
                https_url=f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"
            )
            api = YouTubeTranscriptApi(proxies=proxy_config)
        else:
            api = YouTubeTranscriptApi()

        try:
            fetched = api.fetch(video_id, languages=['en'])
        except Exception:
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
