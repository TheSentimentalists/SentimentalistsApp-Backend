import sys
import logging
import traceback

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

def getText(url):
    from newspaper import Article 
    import nltk
    nltk.download('punkt')
    logger.info(f'getText: initialised Article and ntlk')
    ### Getting the ARTICLE
    try:
        logger.info('getText: Initialising Article...')
        article = Article(url)
        logger.info('getText: Downloading Article...')
        article.download()
        logger.info('getText: Parsing Article...')
        article.parse()
    ### Exception - e.g if URL is "valid" but inexistent, no text will be retrieved
    except Exception as e: 

        logger.info(f'getText: Could not process article result.')

        exception_type, exception_value, exception_traceback = sys.exc_info()
        traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
        err_msg = json.dumps({
            "errorType": exception_type.__name__,
            "errorMessage": str(exception_value),
            "stackTrace": traceback_string
        })
        logger.error(err_msg)
        
        return  {'text': '-1',
                 'header': '', 
                 'summary': '',
                 'keywords':''}

    article.nlp()
    text = article.text

    ### Removing unwanted formatting
    text = text.replace("\n\n", "")
    text = text.replace("Image copyright Getty Images ", "")
    text = text.replace("Image copyright Getty Images/Reuters", "")
    text = text.replace("Image caption ", "")
    text = text.replace("Media playback is unsupported on your device ", "")
    text = text.replace("Media caption ", "")

    return  {'text': text,
             'header': article.title, 
             'summary': article.summary,
             'keywords': article.keywords}
