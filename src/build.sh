#!/bin/bash

# Install modules into ./cache/ folder
if [ -f requirements.txt ]; then 
pip3 install -r requirements.txt --target . --cache-dir ../.cache; 
fi

# Install dev requirements (like boto3) globally
if [ -f build-requirements.txt ]; then pip3 install -r build-requirements.txt; fi

# Run downloadPunkt.py to get that too...
python3 downloadPunkt.py
# ...and remove PY2 assets and .zip to save space!
rm ./nltk_data/tokenizers/punkt.zip
find ./nltk_data/tokenizers/punkt -maxdepth 1 -type f -exec rm -iv {} \;
find ./nltk_data/tokenizers/punkt -maxdepth 1 -type f -delete

# Install spacy modules
python3 -m spacy download en_core_web_sm --target .

# Set XRAY to false in build environment
export AWS_XRAY_SDK_ENABLED=false
