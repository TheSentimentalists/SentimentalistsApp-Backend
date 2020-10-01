## Function: test_getArticle.py
## Author: The Sentimentalists / Ana B Potje
## Date: 30/Sep/2020
##
## Tests the Function "getArticle.py"
## Uses PYTEST framework
###########################################################################################################

import getArticle as getArt   # The code to test

def test_get_top_image():
    url = "https://www.thetimes.co.uk/edition/news/what-happens-if-the-us-election-polls-are-wrong-svwztjvvh"
    Article = getArt.getArticle(url)
    print(Article.top_image)
    assert Article.top_image == "xx" #"https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Ftimes%2Fprod%2Fweb%2Fbin%2F8775f498-02f4-11eb-bce8-b17824147865.jpg?crop=1600%2C900%2C0%2C0&resize=685"
    #assert 1 == 1
