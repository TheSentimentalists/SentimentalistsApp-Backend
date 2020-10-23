#Function: getBiasScore
#Input: credibility, polarity, subjectivity
#Output: BiasScore - indicates possible Bias if an artcle based on credibility, polarity, subjectivity scores
## Author: The Sentimentalists / G C Jyothsna
## Date: 20/Oct/2020
#Polarity: positive or negative emotive words and their positioing in a sentence
#Subjectivity: Inversly proportanal to factual referances in article 
#             (lack of factual referances result in higher subjectivity score)
#Credibility: Rating given per channel/new paper by media observers, autonomus organizations

def getBiasScore(credibility, polarity, subjectivity):
            
    IncredibilityPercent = (100-credibility)
    PolarityPercent = (polarity)*100
    SubjectivityPercent = (subjectivity)*100
    
    if (credibility >= 0):
        BiasIndicator = ((IncredibilityPercent + abs(PolarityPercent) + SubjectivityPercent)/3)
        return BiasIndicator
    else:
        BiasIndicator = ((abs(PolarityPercent)) + SubjectivityPercent)/2
        return BiasIndicator

    response = {'type':'bias','outcome':{'score':BiasIndicator}}
    return response
