## Function: getText
## Input: URL
## Output: Unformatted Text extratcted from the URL
## Author: The Sentimentalists / Ana B Potje
## Date: 24/Sep/2020
##
## This function uses the Python Library Newspaper, which reads the article from the URL,
## remove some unwanted characters and words, and returns the unformatted text.
###########################################################################################################


def getText(url):
    from newspaper import Article
    ### Getting the Text
    try:
        article = Article(url)
        article.download()
        article.parse()
    ### Exception - e.g if URL is "valid" but inexistent, no text will be retrieved
    except Exception as e: 
        #print(e)
        return('-1')
    
    text = article.text
    ### Removing unwanted formatting
    text = text.replace("\n\n", "")
    text = text.replace("Image copyright Getty Images ", "")
    text = text.replace("Image copyright Getty Images/Reuters", "")
    text = text.replace("Image caption ", "")
    text = text.replace("Media playback is unsupported on your device ", "")
    text = text.replace("Media caption ", "")
    return(text);
