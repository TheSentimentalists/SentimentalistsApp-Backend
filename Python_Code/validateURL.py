## Function: validateURL
## Input: URL
## Output: Article
## Author: The Sentimentalists / Ana B Potje
## Date: 28/Sep/2020
##
## This function uses the Python Library Validators, and validates if the URL entered by the user is valid.
## It returns "1" if valid or "-1" if invalid.
###########################################################################################################

def validateURL(url):
    import validators
    valid = validators.url(url)
    if valid==True:
        return(1)
    else:
        return(-1)