## Function: test_getArticle.py
## Author: The Sentimentalists / Ana B Potje
## Date: 30/Sep/2020
##
## Tests the Function "getArticle.py"
## Uses PYTEST framework
###########################################################################################################

import getArticle as getArt   # The code to test

def test_get_article_from_Invalid_URL():
    Article = getArt.getArticle("https://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html")
    assert Article == '-1'

def test_get_top_image():
    Article = getArt.getArticle("https://www.bbc.co.uk/news/business-54371469")
    assert Article.top_image == "https://ichef.bbci.co.uk/news/1024/branded_news/1230F/production/_114711547_54372950.jpg"

def test_get_keywords():
    Article = getArt.getArticle("http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html")
    list_kw = ['test', 'day', 'horrible', 'today', 'daytoday']
    assert Article.keywords.sort() == list_kw.sort()

def test_get_summary():
    Article = getArt.getArticle("http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html")
    assert Article.summary == 'Horrible Day!\nToday is a horrible day.\nToday is a horrible day.\nToday is a horrible day.'
