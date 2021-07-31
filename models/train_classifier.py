# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬import packages▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

print('MESSAGE Step I: Downlaod need pacakages')

import sys
import etl_pipeline

from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import sqlite3
import re
import pickle

import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multioutput import MultiOutputClassifier

from sklearn.metrics import classification_report

# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬HELPER FUNCTIONS▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬


def tokenize(text):
    """[normalization corpus]

    Args:
        text ([Numpy array])

    Returns:
        [Numpy array]
    """
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

def evaluation(X_test, y_test, y, model):
    """[classification report]

    """
    # predict on test data
    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred, target_names=y.columns))

# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬MAIN FUNCTIONS▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

def load_data(MESSAGE_DF_PATH, CAT_DF_PATH):
    """[load the dataset]

    """

    # read in file and clean data
    etl_pipeline.main(MESSAGE_DF_PATH, CAT_DF_PATH)

    # load to database
    con = sqlite3.connect('messages_categories.db')
    df = pd.read_sql_query("SELECT * FROM messages_categories", con)


    # define features and label arrays
    X = df.message
    y = df.iloc[:, 5:]

    return X, y


def build_model():
    """ text processing and model pipeline """
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(tokenizer=tokenize)),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])

    # define parameters for GridSearchCV
    parameters = {
    'tfidf__max_df': (0.5, 0.75, 1.0),
    'tfidf__ngram_range': ((1, 1), (1,2)),
    'tfidf__max_features': (None, 5000,10000),
    'tfidf__use_idf': (True, False)
    }
    
    # create gridsearch object and return as final model pipeline
    model_pipeline = GridSearchCV(pipeline, param_grid=parameters)


    # return model_pipeline
    return pipeline


def train(X, y, model):
    """test split and train model """
    X_train, X_test, y_train, y_test = train_test_split(X, y)


    # fit model
    model.fit(X_train, y_train)

    # output model test results
    evaluation(X_test, y_test, y, model)

    return model


def export_model(model):
    """Export model as a pickle file"""
    Pkl_Filename = "message_category.pkl"  

    with open(Pkl_Filename, 'wb') as file:  
        pickle.dump(model, file)



def run_pipeline(MESSAGE_DF_PATH, CAT_DF_PATH): 
    """ The main function to traing model and export it"""
    
    print('MESSAGE Step II: Data Wrangling')
    X, y = load_data(MESSAGE_DF_PATH, CAT_DF_PATH)  # run ETL pipeline
    
    print('MESSAGE Step III: build model pipeline')
    model = build_model()  

    print('MESSAGE Step IV: train model pipeline')
    model = train(X, y, model)  
    
    print('MESSAGE Step V: save model')
    export_model(model) 

# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬


if __name__ == '__main__':
    if len(sys.argv) == 3:
        
        MESSAGE_DF_PATH, CAT_DF_PATH = sys.argv[1:]        
        run_pipeline(MESSAGE_DF_PATH, CAT_DF_PATH) 

    else: 
        print(""" ERROR: Please provide the filepaths of the messages and categories 
            datasets as the first and second argument respectively """)

    
