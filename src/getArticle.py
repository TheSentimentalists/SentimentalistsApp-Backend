## Function: getArticle
## Input: URL
## Output: Article
## Author: The Sentimentalists / Ana B Potje
## Date: 24/Sep/2020
##
## This function uses the Python Library Newspaper, which reads the article from the URL.
## It then applies the "nlp()" function to perform natural language processing on the news article.
##
## Use of this function:
##   news_article = getArticle("https://www.bbc.co.uk/news/uk-54234084")
##   news_article.top_image
##   >>> https://ichef.bbci.co.uk/images/ic/1024x576/p08s2yp9.jpg
##   news_article.keywords
##   >>> ['action', '50000', 'patrick', 'face', 'covid19', 'restrictions', 'governments', ...]
##   news_article.summary
##   >>> Sir Patrick Vallance said that would be expected to lead to about "200-plus deaths per day" a 
##       month after that. On Monday, a further 4,368 daily cases were reported in the UK, up from 3,899....
###########################################################################################################

 
def getArticle(url):
    from newspaper import Article

    ## use the output to get features such as "article.top_image", "article.keywords", "article.summary", etc  
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return(article)