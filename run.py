import warnings
warnings.filterwarnings('ignore')

import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


def tokenize(text):
    # normalizarion
    text = text.lower()
    text = text.strip()

    # Punctuation Removal
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    
    # word_tokenize
    tokens = word_tokenize(text)

    # Remove stop words
    words = [token for token in tokens if token not in stopwords.words("english")]

    # Reduce words to their root form
    lemmed = [WordNetLemmatizer().lemmatize(w) for w in words]

    # re-create document from filtered lemmed
    doc = ' '.join(lemmed)
    
    return doc


from MessageCategory import app
app.run(host='localhost', port=3001, debug=True)