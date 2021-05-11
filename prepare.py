import nltk
import unicodedata
import re

#------------------------------------------------------------------------------------------------------------------------------------------------------

ADDITIONAL_STOPWORDS = ['r', 'u', '2', 'ltgt']

def clean(readme_contents):
    'A simple function to cleanup text data'
    wnl = nltk.stem.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english') + ADDITIONAL_STOPWORDS
    text = (unicodedata.normalize('NFKD', readme_contents)
             .encode('ascii', 'ignore')
             .decode('utf-8', 'ignore')
             .lower())
    words = re.sub(r'[^\w\s]', '', readme_contents).split()
    return [wnl.lemmatize(word) for word in words if word not in stopwords]

#------------------------------------------------------------------------------------------------------------------------------------------------------