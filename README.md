# SentimentalistsApp-Backend

The backend service for [The Sentimentalists](https://thesentimentalists.github.io) article analysis service.<br />
The source code was developed in PYTHON. <br />
The APP was then built and deployed on AWS Lambda.<br />

![Image of Backend](https://github.com/TheSentimentalists/SentimentalistsApp-Backend/blob/master/System_Overview.jpg?raw=true)

## Folder Structure:

The SENTIMENTALISTSAPP-BACKEND is divided into the following folders:

### `infra \ prod`
Contains the Terraform files:<br />
  -  main.tf<br />
  -  variables.tf<br />

### `src`
Contains the source code of our Python modules.<br />
  -  downloadPunkt.py<br />
     Downloads NLTK PUNKT, which is used by TextBlob library, in order to reduce the size of the package passed in the automation to AWS Lambda.<br />

  -  getBiasScore.py<br />
     Calculates the TRUST SCORE, based on the credibility, polarity, subjectivity values.<br />

  -  getCredibilityScore.py<br />
     Calls the API Gate Source Credibility passing the URL. Returns the URL Credibility Score, Category (Left Center, Fake News, ... and the Source which rated the website (Media Bias / Fact Check, etc)..py.<br />

  -  getSecret.py<br />
     Calls AWS Secret Manager and returns the requested secret as a dict of key/value pairs.<br />

  -  getText.py<br />
     Calls the Python library "Newspaper", which retrieves the text (article) from an URL.
     Returns the article TEXT, HEADER, SUMMARY, KEYWORDS and TOP_IMAGE of the news article.<br />

  -  lambda_function.py<br />
     Main module of our backend app. Firstly it validates the URL, then it calls the following Python modules:<br />
     1) getCredibilityScore.py<br />
     2) sentimentAnalysis.py<br />
     3) getBiasScore.py<br />
     4) spacyMatcher.py<br />
 
     Each of these modules returns results that will populate our JSON file, which will be sent to the frontend via AWS Lambda.<br />

  -  sentimentAnalysis.py<br />
     Reads an URL, then calls the function "getText" to convert the HTML text into  an unformatted text. Then it calls the Python <br />
     Library TextBlob, which analyses the "sentiment" of the text. It finally returns the polarity and subjectivity of the whole text.<br />

  -  spacyMatcher.py<br />
     Calls the Python Library Spacy with a TEXT to be analysed and a specific TAG (or '' for ALL TAGS). Lambda_Function.py calls spacyMatcher with TAG = '', so ALL TAGS are returned. Please find below the list of tags currently used. The output of this function is a list with dictionary pairs: {'type' : tag, 'topic' : obj}.<br />
      PERSON - People, including fictional.<br />
      ORG - Companies, agencies, institutions, etc.<br />
      GPE - Countries, cities, states.<br />
      PERCENT - Percentage, including ”%“.<br />
      LANGUAGE - Any named language.<br />
      DATE - Absolute or relative dates or periods.<br />
      TIME - Times smaller than a day.<br />
      LOC - Non-GPE locations, mountain ranges, bodies of water.<br />
      NORP - Nationalities or religious or political groups.<br />
      EVENT - Named hurricanes, battles, wars, sports events, etc.<br />
      WORK_OF_ART - Titles of books, songs, etc.<br />
      MONEY - Monetary values, including unit.<br />
      QUANTITY - Measurements, as of weight or distance.<br />
      ORDINAL - “first”, “second”, etc.<br />
      CARDINAL - Numerals that do not fall under another type (not ordinal, quantity ..)<br />
    PS: Our APP Frontend is currently Using the following spaCy tags: PERSON, ORG, GPE, EVENT and WORK_OF_ART.<br />

The following files are used in the automation, installing objects, compressing / deleting them or pointing to the Python libraries that must be installed:<br />
  -  build-requirements.txt<br />
  -  build.sh<br />
  -  package.sh<br />
  -  requirements.txt<br />

### `tests`
Contains the Python modules used to run the tests (PYTEST library).<br />
We are currently running 50 tests, as shown below:
  -  test_checkCredibilityScore.py  (2 tests)<br />
  -  test_getBiasScore.py           (2 tests)<br />
  -  test_getSecret.py              (2 tests)<br />
  -  test_getText.py                (6 tests)<br />
  -  test_lambda_handler.py         (15 tests)<br />
  -  test_sentimentAnalysis.py      (7 tests)<br />
  -  test_spacyMatcher.py           (16 tests)<br />

### `INSTALL.md (file)`
The file INSTALL.md contains commands used to create the local anaconda environment, as well as settings used to enable the PYTEST execution and important environment variables locally set.

### `SCOPE.md (file)`
The file SCOPE.md has a list of the libraries and APIs used in the backend code. It also has a list of ideas that can be implemented in future MVPs.
