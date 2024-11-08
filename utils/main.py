from utils.get_transcript import * 
from utils.model import * 


def get_output(url,tone):
    try:
        transcripts = get_transcript_txt(url)
        article = get_article(transcripts,tone)
        return article
    except Exception as e:
        return f"An error occurred: {str(e)}"
