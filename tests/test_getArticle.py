## Function: test_getArticle.py
## Author: The Sentimentalists / Ana B Potje
## Date: 30/Sep/2020
##
## Tests the Function "getArticle.py"
## Uses PYTEST framework
###########################################################################################################

import getArticle as getArt   # The code to test

def test_get_top_image():
    Article = getArt.getArticle("https://www.bbc.co.uk/news/business-54371469")
    assert Article.top_image == "https://ichef.bbci.co.uk/news/1024/branded_news/1230F/production/_114711547_54372950.jpg"

def test_get_keywords():
    Article = getArt.getArticle("https://www.bbc.co.uk/news/business-54371469")
    list_kw = ['loyalty', 'mobile', 'dont', 'chapman', 'vulnerable', 'impossible', 'paying', 'customers', 'price', 'does', 'computer', 'shopping', 'mrs', 'insurance']
    assert Article.keywords == list_kw

def test_get_summary():
    Article = getArt.getArticle("https://www.bbc.co.uk/news/business-54371469")
    summary = 'But Mrs Chapman was lucky.\nThe widow, from County Durham, does not have a computer and does not know how to operate one.\n"I was surprised," says Mrs Chapman.\nBusinesses giving vulnerable customers targeted help?\nThat would still prevent people such as Mrs Chapman, who do not have internet access, from getting the very cheapest deals.'
    assert Article.summary == summary
