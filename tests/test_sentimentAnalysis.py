## Function: test_sentimentAnalysis.py
## Author: The Sentimentalists / Ana B Potje
## Date: 05/10/2020
##
## Tests the Function "sentimentAnalysis.py", uses the function "getText.py" to get the text from the URL
## Uses PYTEST framework
###########################################################################################################

import sentimentAnalysis as sentAnalysis   # The code to test

def test_Polarity():
    url = 'http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html'
    analysed_text = sentAnalysis.sentimentAnalysis(url)
    assert analysed_text.sentiment.polarity == -1.0

def test_Subjectivity():
    url = 'http://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html'
    analysed_text = sentAnalysis.sentimentAnalysis(url)
    assert analysed_text.sentiment.subjectivity == 1.0

def test_Sentiment_for_Invalid_url():
    url = 'https://sentimentalists-tests.s3-website.eu-west-2.amazonaws.com/today.html'
    analysed_text = sentAnalysis.sentimentAnalysis(url)
    assert analysed_text == ''
