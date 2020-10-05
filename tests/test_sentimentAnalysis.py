## Function: test_sentimentAnalysis.py
## Author: The Sentimentalists / Ana B Potje
## Date: 05/10/2020
##
## Tests the Function "sentimentAnalysis.py", uses the function "getText.py" to get the text from the URL
## Uses PYTEST framework
###########################################################################################################

import sentimentAnalysis as sentAnalysis   # The code to test

def test_Polarity():
    url = "https://www.bbc.co.uk/news/uk-54234084"
    analysed_text = sentAnalysis.sentimentAnalysis(url)
    assert analysed_text.sentiment.polarity == 0.055258047508047504

def test_Subjectivity():
    url = "https://www.bbc.co.uk/news/uk-54234084"
    analysed_text = sentAnalysis.sentimentAnalysis(url)
    assert analysed_text.sentiment.subjectivity == 0.4314774392274392
