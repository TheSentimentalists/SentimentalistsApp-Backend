## Function: spacyMatcher
## Input: TEXT and TAG (PERSON, ORG, GPE, etc)
## Output: Set with all names (of person, countries ..) found in the text
## Author: The Sentimentalists / Ana B Potje
## Date: 15/Oct/2020
##
## This function uses the Python Library Spacy. The user will input an URL and a "TAG" such as:
##    PERSON - People, including fictional.
##    ORG - Companies, agencies, institutions, etc.
##    GPE - Countries, cities, states.
##    PERCENT - Percentage, including ”%“.
##    LANGUAGE - Any named language.
##    DATE - Absolute or relative dates or periods.
##    TIME - Times smaller than a day.
##    LOC - Non-GPE locations, mountain ranges, bodies of water.
##    NORP - Nationalities or religious or political groups.
##    EVENT - Named hurricanes, battles, wars, sports events, etc.
##    WORK_OF_ART - Titles of books, songs, etc.
##    MONEY - Monetary values, including unit.
##    QUANTITY - Measurements, as of weight or distance.
##    ORDINAL - “first”, “second”, etc.
##    CARDINAL - Numerals that do not fall under another type (not ordinal, quantity ..)
##
## It will return a list with distinct values of all occurrences of that entity in the text.
###########################################################################################################

from aws_xray_sdk.core import xray_recorder

@xray_recorder.capture('spacyMatcher')

def spacyMatcher(text, tag): 
    import spacy

    ret_set = []
    if text != '-1':
        ### analysing the text 
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
    
        interestWords = [(ent.text, ent.label_) for ent in doc.ents]
        list_all_values = [tup[0] for tup in interestWords if any(i in tup for i in [tag])]
        ret_set = set(list_all_values)

    return(ret_set) ### RETURNS A SET
