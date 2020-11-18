from aws_xray_sdk.core import xray_recorder
import sys
import logging
import traceback
from newspaper import Article
import nltk

logger = logging.getLogger()
logger.setLevel(logging.INFO)
nltk.data.path.append("./nltk_data")


@xray_recorder.capture('getText')
def get_text(url):

    """
    This function uses the Python Library Newspaper, which reads the article
    from the URL, remove some unwanted characters and words, so the unformatted
    text is stored in a variable "text". It then applies the "nlp()" function
    to perform natural language processing on the news article.

    The objects "text", "header", "summary", "keywords" and "image" are the
    output of this function.
    """

    logger.info(f'getText: initialised Article and ntlk')
    try:
        print("getText: Initialising Article...")
        subsegment = xray_recorder.begin_subsegment('getText: init article')
        article = Article(url)
        xray_recorder.end_subsegment()

        print("getText: Downloading Article...")
        subsegment = xray_recorder.begin_subsegment('getText: '
                                                    'download article')
        article.download()
        xray_recorder.end_subsegment()

        print("getText: Parsing Article...")
        subsegment = xray_recorder.begin_subsegment('getText: parse article')
        article.parse()
        xray_recorder.end_subsegment()
    except Exception as e:
        print("getText: Exception: " + str(e))
        return {'text': '-1',
                'header': '',
                'summary': '',
                'keywords': '',
                'image': ''}

    subsegment = xray_recorder.begin_subsegment('getText: nlp article')
    article.nlp()
    xray_recorder.end_subsegment()
    text = article.text

    text = text.replace("\n\n", "")
    text = text.replace("Image copyright Getty Images ", "")
    text = text.replace("Image copyright Getty Images/Reuters", "")
    text = text.replace("Image caption ", "")
    text = text.replace("Media playback is unsupported on your device ", "")
    text = text.replace("Media caption ", "")

    result = {'text': text,
              'header': article.title,
              'summary': article.summary,
              'keywords': article.keywords,
              'image': article.top_image}

    return result
