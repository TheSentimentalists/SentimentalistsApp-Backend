#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Function: test_getBiasScore.py
## Author: The Sentimentalists / G C Jyothsna
## Date: 20/10/2020
## Tests the Function "getBiasScore.py"
## Uses PYTEST framework
###########################################################################################################

import getBiasScore as getBiasScr    # The code to test 

def test_getBiasScore_withoutvalid_credibility():
    result_score = {'type': 'bias', 'outcome': {'score': 50.0}}
    assert getBiasScr.getBiasScore(-1,-1,0) == result_score

def test_getBiasScore_with_credibility():
    result_score = {'type': 'bias', 'outcome':{'score':66.66666666666667}}
    assert getBiasScr.getBiasScore(0,-1,0) == result_score

