#Function: getBiasScore
#Input: credibility, polarity, subjectivity from SentimentAnalysis, getCredibility
#Output: BiasScore - indicates possible Bias if an article based on credibility, polarity, subjectivity scores
## Author: The Sentimentalists / G C Jyothsna
## Date: 20/Oct/2020
#Polarity: positive or negative emotive words and their positioning in a sentence#Subjectivity: Inversely proportional to factual references in article 
#             (lack of factual references result in higher subjectivity score)
#Credibility: Rating given per channel/new paper by media observers, autonomous organizations
def getBiasScore(credibility, polarity, subjectivity):
            
    IncredibilityPercent = (100-credibility)
    PolarityPercent = (polarity)*100
    SubjectivityPercent = (subjectivity)*100
    
    if (credibility >= 0):
        BiasIndicator = ((IncredibilityPercent + abs(PolarityPercent) + SubjectivityPercent)/3)
    else:
        BiasIndicator = ((abs(PolarityPercent)) + SubjectivityPercent)/2

    response = {'type':'bias','outcome':{'score':BiasIndicator}}
    return response
