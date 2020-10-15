## Function: spacyMatcher
## Input: URL and TAG (PERSON, ORG, GPE)
## Output: Set with all names (of person, countries ..) found in the text
## Author: The Sentimentalists / Ana B Potje
## Date: 15/Oct/2020
##
## This function uses the Python Library Spacy. The user will input an URL and a "TAG" such as:
##    PERSON - People, including fictional.
##    ORG - Companies, agencies, institutions, etc.
##    GPE - Countries, cities, states.
## It will return a list with distinct values of all occurrences of that entity in the text.
###########################################################################################################

def spacyMatcher(url, tag): 
    import getText as getTxt
    import spacy

    text = getTxt.getText(url)
    ret_set = []
    if text != '-1':
        ### analysing the text 
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
    
        interestWords = [(ent.text, ent.label_) for ent in doc.ents]
        list_all_values = [tup[0] for tup in interestWords if any(i in tup for i in [tag])]
        ret_set = set(list_all_values)

    return(ret_set) ### RETURNS A SET
