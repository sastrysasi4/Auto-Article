import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from operator import itemgetter


## llm model
GOOGLE_API_KEY= os.getenv('GOOGLE_API_KEY') 
genai.configure(api_key=GOOGLE_API_KEY)
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.3)


template = """
Act as an expert copywriter specializing in content optimization for SEO. Your task is to take a given YouTube transcript and transform it into a well-structured and engaging article. Your objectives are as follows:

Content Transformation: Begin by thoroughly reading the provided YouTube transcript. Understand the main ideas, key points, and the overall message conveyed.

Sentence Structure: While rephrasing the content, pay careful attention to sentence structure. Ensure that the article flows logically and coherently.

Keyword Identification: Identify the main keyword or phrase from the transcript. It's crucial to determine the primary topic that the YouTube video discusses.

Keyword Integration: Incorporate the identified keyword naturally throughout the article. Use it in headings, subheadings, and within the body text. However, avoid overuse or keyword stuffing, as this can negatively affect SEO.

Unique Content: Your goal is to make the article 100 percent unique. Avoid copying sentences directly from the transcript. Rewrite the content in your own words while retaining the original message and meaning.

SEO Friendliness: Craft the article with SEO best practices in mind. This includes optimizing meta tags (title and meta description), using header tags appropriately, and maintaining an appropriate keyword density.

Engaging and Informative: Ensure that the article is engaging and informative for the reader. It should provide value and insight on the topic discussed in the YouTube video.

Proofreading: Proofread the article for grammar, spelling, and punctuation errors. Ensure it is free of any mistakes that could detract from its quality.

By following these guidelines, create a well-optimized, unique, and informative article that would rank well in search engine results and engage readers effectively.

Transcript:{transcript}
Tone of the output article : {tone}
The output should in Markdown format.
"""
prompt = ChatPromptTemplate.from_template(template)


retrieval_chain = (
    {
        "transcript": itemgetter("transcript"),
        "tone" : itemgetter("tone")
    }
    | prompt
    | model
    | StrOutputParser()
)


def get_article(transcripts,tone, his=''):
    model_result = retrieval_chain.invoke({"transcript": transcripts, "tone": tone})
    return model_result