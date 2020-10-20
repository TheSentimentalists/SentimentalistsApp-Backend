#Function: getBiasScore
#Input: credibility, polarity, subjectivity
#Output: BiasScore - indicates possible Bias if an artcle based on credibility, polarity, subjectivity scores
#Polarity: positive or negative emotive words and their positioing in a sentence
#Subjectivity: Inversly proportanal to factual referances in article 
#             (lack of factual referances result in higher subjectivity score)
#Credibility: Rating given per channel/new paper by media observers, autonomus organizations

def getBiasScore(credibility, polarity, subjectivity):

    IncredibilityPercent = (100-credibility)
    PolarityPercent = (polarity)*100
    SubjectivityPercent = (subjectivity)*100

    BiasIndicator = ((IncredibilityPercent + abs(PolarityPercent) + SubjectivityPercent)/3)

    response = {'type':'bias','outcome':{'score':BiasIndicator}}
    return response
