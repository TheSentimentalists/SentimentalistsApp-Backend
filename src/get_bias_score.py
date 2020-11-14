def get_bias_score(credibility, polarity, subjectivity):

    """
    Input: credibility, polarity, subjectivity from SentimentAnalysis,
           getCredibility
    Output: BiasScore - indicates possible Bias if an article based on
            credibility, polarity, subjectivity scores
    Polarity: positive or negative emotive words and their positioning in a
              sentence#Subjectivity: Inversely proportional to factual
              references in article (lack of factual references result in
              higher subjectivity score)
    Credibility: Rating given per channel/new paper by media observers,
                 autonomous organizations
    """

    incredibility_percent = (100-credibility)
    polarity_percent = (polarity)*100
    subjectivity_percent = (subjectivity)*100

    if (credibility >= 0):
        bias_indicator = ((incredibility_percent + abs(polarity_percent) +
                          subjectivity_percent)/3)
    else:
        bias_indicator = ((abs(polarity_percent)) + subjectivity_percent)/2

    response = {'type': 'bias', 'outcome': {'score': bias_indicator}}
    return response
