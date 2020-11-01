from aws_xray_sdk.core import xray_recorder
import sys
import logging
import traceback
from newspaper import Article 
import nltk

## Function: getText
## Input: URL
## Output: Unformatted TEXT extracted from the URL and ARTICLE
## Author: The Sentimentalists / Ana B Potje
## Date: 24/Sep/2020
## Last Modified: 22/Oct/2020
##
## This function uses the Python Library Newspaper, which reads the article from the URL,
## remove some unwanted characters and words, so the unformatted text is stored in a variable "text".
## It then applies the "nlp()" function to perform natural language processing on the news article.
##
## The objects "text" and "article" are the output of this function.
##
## PS: Use of the "article" object:
##   news_article = getArticle("https://www.bbc.co.uk/news/uk-54234084")
##   news_article.top_image
##   >>> https://ichef.bbci.co.uk/images/ic/1024x576/p08s2yp9.jpg
##   news_article.keywords
##   >>> ['action', '50000', 'patrick', 'face', 'covid19', 'restrictions', 'governments', ...]
##   news_article.summary
##   >>> Sir Patrick Vallance said that would be expected to lead to about "200-plus deaths per day" a 
##       month after that. On Monday, a further 4,368 daily cases were reported in the UK, up from 3,899....
###########################################################################################################

logger = logging.getLogger()
logger.setLevel(logging.INFO)
nltk.data.path.append("./nltk_data")

@xray_recorder.capture('getText')
def getText(url):
    
    logger.info(f'getText: initialised Article and ntlk')
    ### Getting the ARTICLE
    try:
        print("getText: Initialising Article...")
        subsegment = xray_recorder.begin_subsegment('getText: init article')
        article = Article(url)
        xray_recorder.end_subsegment()

        print("getText: Downloading Article...")
        subsegment = xray_recorder.begin_subsegment('getText: download article')
        article.download()
        xray_recorder.end_subsegment()

        print("getText: Parsing Article...")
        subsegment = xray_recorder.begin_subsegment('getText: parse article')
        article.parse()
        xray_recorder.end_subsegment()
    ### Exception - e.g if URL is "valid" but inexistent, no text will be retrieved
    except Exception as e: 
        print("getText: Exception: " + str(e))
        return  {'text': '-1',
                 'header': '', 
                 'summary': '',
                 'keywords':''}

    subsegment = xray_recorder.begin_subsegment('getText: nlp article')
    article.nlp()
    xray_recorder.end_subsegment()
    text = article.text

    ### Removing unwanted formatting
    text = text.replace("\n\n", "")
    text = text.replace("Image copyright Getty Images ", "")
    text = text.replace("Image copyright Getty Images/Reuters", "")
    text = text.replace("Image caption ", "")
    text = text.replace("Media playback is unsupported on your device ", "")
    text = text.replace("Media caption ", "")

    result = {'text': text,
             'header': article.title, 
             'summary': article.summary,
             'keywords': article.keywords}

    if article.top_image != "":
        result['image'] = article.top_image       

    return result
