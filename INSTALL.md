###  `Creating environment c:\anaconda3\envs\sentim`
conda create -n sentim python=3 jupyter requests validators textblob

###  `Installing extra packages`
$ conda install -c conda-forge pytest<br />
$ conda activate sentim<br />
$ conda install -c conda-forge newspaper3k<br />
$ conda install -c conda-forge nltk <br />
$ conda install -c conda-forge boto3<br />
$ pip install vaderSentiment<br />
$ python -m ipykernel install<br />
$ pip install aws-xray-sdk<br /> 

PS: Some of the packages below, such as vaderSentiment, were used in our tests but not implemented in our final code

###  `Installing Spacy package and objects`
$ conda install -c conda-forge spacy<br />
$ python -m spacy download en_core_web_sm<br />
$ python -m spacy download en_core_web_md<br />

###  `Environment Variables`
* added 3 directories in the PATH variable:<br />
D:\Anaconda3 ; D:\Anaconda3\Scripts ; D:\Anaconda3\Library\bin<br />
* Included on the TOP of the PATH variable:<br />
c:\Anaconda3\envs\sentim            =>> Python<br />
c:\Anaconda3\envs\sentim\Scripts    =>> Pytest<br />
c:\Anaconda3\Scripts                =>> Conda<br />
* Created a new Env variable to disable AWS_XRAY locally:<br />
AWS_XRAY_SDK_ENABLED = false<br />

###  `Pytest settings and linting`
Created PYTHONPATH environment variable pointing to the "src" directory for Pytest:<br />
     PYTHONTEST = "D:\AATechReturners\Sentimentalists\backend\SentimentalistsApp-Backend\src"<br />
Included empty files "__init__.py" in the test and src directories (required for Pytest)<br />

Created the file "setup.py" under the directory "SentimentalistsApp-Backend":<br />

#!/usr/bin/env python3<br />
from setuptools import setup, find_packages<br />
setup(name="utils", packages=find_packages())<br />

All code in the repo is formatted to PEP8 standards, please install the packages below to ensure consistency:
$ pip install pep8
$ pip install pylint
$ conda install --name sentim pydocstyle -y
$ conda install --name sentim pycodestyle -y
