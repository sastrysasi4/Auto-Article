from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

## Getting video id from the youtube link
def get_video_id(url):
    video_id = url.split("v=")[1].split("&")[0]
    # print(url)
    return video_id

## Getting transcript from video id
def get_transcript_txt(url):
    video_id = get_video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id ,languages=['en'])
    # print(transcript)

    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript) # turns the transcript into .txt file.
    # print(text_formatted)
    return text_formatted
