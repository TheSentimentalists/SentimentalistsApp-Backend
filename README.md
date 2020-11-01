# SentimentalistsApp-Backend

The backend service for [The Sentimentalists](https://thesentimentalists.github.io) article analysis service. Deployed on AWS Lambda.

## Folder Structure:

The SENTIMENTALISTSAPP-BACKEND is divided into the following folders:

### `infra \ prod`
Contains the Terraform files:<br />
  -  main.tf<br />
  -  variables.tf<br />

### `src`
Contains the source code of our Python modules.<br />
  -  getBiasScore.py<br />
  -  getCredibilityScore.py<br />
  -  getSecret.py<br />
  -  getText.py<br />
  -  lambda_function.py<br />
  -  sentimentAnalysis.py<br />
  -  spacyMatcher.py<br />
     (Frontend is currently Using the following spaCy tags: PERSON, GPE, ORG, WORK_OF_ART, EVENT)

The following two files are used in the automation, pointing to the Python libraries that must be installed:<br />
  -  build-requirements.txt<br />
  -  requirements.txt<br />

### `tests`
Contains the Python modules used to run the tests (PYTEST library).<br />
  -  test_checkCredibilityScore.py<br />
  -  test_getBiasScore.py<br />
  -  test_getSecret.py<br />
  -  test_getText.py<br />
  -  test_lambda_handler.py<br />
  -  test_sentimentAnalysis.py<br />
  -  test_spacyMatcher.py<br />

### `INSTALL.md (file)`
The file INSTALL.md contains commands used to create the local anaconda environment, as well as settings used to enable the PYTEST execution and important environment variables locally set.

### `SCOPE.md (file)`
The file SCOPE.md has a list of the libraries and APIs used in the backend code. It also has a list of ideas that can be implemented in future MVPs.
