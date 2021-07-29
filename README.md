# Disaster Response Pipeline Project



## Introduction

After a disaster, responsible agencies typically receive millions of direct or social media communications just when disaster response organizations are least able to filter and select the most important messages. Often, only one in a thousand messages is relevant for disaster response professionals. Typically, in response to disasters, Different organizations take care of different parts of the problem. One organization takes care of water, another takes care of blocked roads, another takes care of medical supplies.



## Objectives

This Project is a part of Data Science Nanodegree Program by Udacity in collaboration with Figure Eight. This project aims to develop a computational model based on the Natural Language Processing (NLP) to classify messages and identify needs after a disaster.



## Description

When looking at the data, these are the categories that have selected for the data set. The Figure Eight is used for many of the disasters from which messages were pulled, then combined the data sets and re-labeled them to have consistent labels across different disasters. This is to allow to investigate the different trends that can found and build supervised machine learning models to help respond to future disasters. The aim of the project is to build a Natural Language Processing (NLP) tool that categorize disaster messages.

The Project is divided in the following Sections:

1. Data Processing, ETL Pipeline to extract data from source, clean data and save them in a proper database structure.
2. Machine Learning Pipeline to train and tunning a model able to classify text messages into appropriate categories.
3. Web App to show model results in real time.



## Dependences

```txt
click==8.0.1
Flask==2.0.1
greenlet==1.1.0
itsdangerous==2.0.1
Jinja2==3.0.1
joblib==1.0.1
MarkupSafe==2.0.1
nltk==3.6.2
numpy==1.21.1
pandas==1.3.1
plotly==5.1.0
python-dateutil==2.8.2
pytz==2021.1
regex==2021.7.6
scikit-learn==0.24.1
scipy==1.7.0
six==1.16.0
sklearn==0.0
SQLAlchemy==1.4.22
tenacity==8.0.1
threadpoolctl==2.2.0
tqdm==4.61.2
Werkzeug==2.0.1
WTForms==2.3.3
```

## Installing dependences

```bash
pipenv install -r ./requirements.txt
```

## Run Program

- Run the following commands in the project's root directory to set up your database and model.

  ```bash
  python models/train_classifier.py messages.csv categories.csv
  ```

- Run the following commands in the project’s root directory to run Web Application 

  ```bash
  python run.py
  ```

  

## File Structure

 

```
├── Data
│   └── messages_categories.db
├── MessageCategory
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       ├── go.html
│       ├── includes
│       │   ├── _formhelpers.html
│       │   └── _navbar.html
│       ├── layout.html
│       └── master.html
├── models
│   ├── categories.csv
│   ├── etl_pipeline.py
│   ├── helper.py
│   ├── message_category.pkl
│   ├── messages_categories.db
│   ├── messages.csv
│   └── train_classifier.py
│   └── train_classifier.py
├── visualization
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   ├── visualization.cpython-36.pyc
    │   ├── viz.cpython-36.pyc
    │   └── viz.cpython-38.pyc
    └── viz.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
├── run.py
├── setup.py

```

## Acknowledgements

- [Udacity](https://www.udacity.com/) for providing such a complete Data Science Nanodegree Program
- [Figure Eight](https://www.figure-eight.com/) for providing messages dataset to train my model

