# - app
# | - template
# | |- master.html  # main page of web app
# | |- go.html  # classification result page of web app
# |- run.py  # Flask file that runs app

# - data
# |- disaster_categories.csv  # data to process 
# |- disaster_messages.csv  # data to process
# |- process_data.py
# |- InsertDatabaseName.db   # database to save clean data to

# - models
# |- train_classifier.py
# |- classifier.pkl  # saved model 
# - README.md

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