from aws_xray_sdk.core import xray_recorder
import sys
import logging
import traceback
import get_text as get_txt
from textblob import TextBlob

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@xray_recorder.capture('sentimentAnalysis')
def sentiment_analysis(url):
    """
    Input: URL
    Output: Header, Summary, Keywords, Image, Polarity and Subjectivity

    This function reads an URL, then calls the function "getText" to convert
    the HTML text into an unformatted text. This functionn returns the text,
    and the Header, Summary, Keywords and Image.
    Then it calls the Python Library TextBlob, which analyses the "sentiment"
    of the text. The returned variable "testimonial" is then used to check
    the sentiment of the whole text (testimonial.sentiment).
    """

    logger.info(f'SentimentAnalysis: initialised')

    dict_return = get_txt.get_text(url)
    testimonial = ''

    if dict_return['text'] != '-1':
        testimonial = TextBlob(dict_return['text'])
        dict_return['polarity'] = testimonial.sentiment.polarity
        dict_return['subjectivity'] = testimonial.sentiment.subjectivity

    return dict_return
