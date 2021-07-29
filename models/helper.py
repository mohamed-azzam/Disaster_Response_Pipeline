import pandas as pd

def split_col(col, delimiter=";"):
    """split string to columns on specific delimiter"""
    return col.str.split(";", expand=True)

def column_name(df):
    """find the columns name of categories df and return new df"""

    # select the first row of the categories dataframe
    row = df.iloc[0]

    category_colnames = row.apply(lambda x: x.split('-')[0])

    df.columns = category_colnames

    return df

def convert_type(df, columns, type='int'):
    """convert the type of column"""
    for column in columns:
        # set each value to be the last character of the string
        df[column] = df[column].apply(lambda x: x.split('-')[1])
        
        # convert column from string to numeric
        df[column] = df[column].astype(type)    

    return df

