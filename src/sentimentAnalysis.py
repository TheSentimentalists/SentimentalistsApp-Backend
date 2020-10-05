## Function: sentimentAnalysis
## Input: URL
## Output: Analysed Text (or testimonial)
## Author: The Sentimentalists / Ana B Potje
## Date: 24/Sep/2020
##
## This function reads an URL, then calls the function "getText" to convert the HTML text into 
## an unformatted text. Then it calls the Python Library TextBlob, which analyses the "sentiment"
## of the text. The returned variable "testimonial" can be used:
##
## 1) To check the sentiment of the whole text (testimonial.sentiment) or
## 2) To check the sentiment for each sentence of the text (testimonial.sentences)
##
##  The Sentiment returns the features POLARITY and SUBJECTIVITY, e.g:
##     analysed_text = sentimentAnalysis("https://www.bbc.co.uk/news/uk-54234084")
##     analysed_text.sentiment
##     >>> Sentiment(polarity=0.055258047508047504, subjectivity=0.4314774392274392)
##  Or
##     analysed_text = sentimentAnalysis("https://www.bbc.co.uk/news/uk-54234084")
##     for sentence in analysed_text.sentences:
##        print(sentence.sentiment)
##        print(sentence)
##        >>> Sentiment(polarity=0.012603305785123968, subjectivity=0.3431818181818182)
##        >>> Chief Scientific Officer Sir Patrick Vallance says measures must be taken to stop the...
###########################################################################################################

def sentimentAnalysis(url):
    import getText as getTxt
    from textblob import TextBlob

    text = getTxt.getText(url)
    ### analysing the text 
    testimonial = TextBlob(text)
    ## use the output as "testimonial.sentiment" or "testimonial.sentences"
    return(testimonial)
