# Issues

**Issue #1 - URL Contains Multiple Articles**
- We need to investigate the possibility of a user entering an URL that possibly contains more than 1 article.
- Example: url = "https://www.thesun.co.uk/news/12710493/jeremy-clarkson-task-force-fix-a-bridge/"
- How likely is this issue to happen (maybe only on "SUN" website?)
- In case this happens:
   * Reject the URL (how?)
   * Send a message on the screen warning that the link contains several articles?

**Issue #2 - Analyse URL language
- If the URL is from a foreign website, the code still analyse its sentiment (polarity / subjectivity)
- As an improvement, we can capture the language and throw an error if the language is not "English"

**Issue #3 - getText function needs improvement
- BBC articles (between other ...) are not properly converted to TEXT because of titles under its photos etc.
- SPACY.MATCHER (PHRASEMATCHER) return wrong values because of this issue.

**Issue #4 - Free TEXT typing (improvement)
- to enable thr users to see effectively the sentiment analysis results when a simple sentence is typed in the screen.
- BIAS SCORE must not include "check credibility" call in this case.