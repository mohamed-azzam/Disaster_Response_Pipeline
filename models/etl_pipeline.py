# import packages
import sys
import pandas as pd
from sqlalchemy import create_engine
import helper



def load_data(MESSAGE_DF_PATH, CAT_DF_PATH):
    """load the csv dataset"""
    message_df =  pd.read_csv(f'{MESSAGE_DF_PATH}')
    categories_df =  pd.read_csv(f'{CAT_DF_PATH}')

    return message_df, categories_df

def merge_datesets(dataSet_1, dataSet_2, on='id'):
    """merge the datasets"""
    df = pd.merge(dataSet_1,dataSet_2,on=on)

    return df


def transform_category_col(col):
    """transform category column"""

    # split the cat columns
    cat_df = helper.split_col(col)

    # find the column name 
    cat_df = helper.column_name(cat_df)

    # convert the type to int
    cat_df = helper.convert_type(cat_df, cat_df.columns)

    return cat_df


def df_transform(df, cat_df):
    """make transformation to df"""

    # drop cat col
    df.drop(['categories'], axis=1, inplace=True)

    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df,cat_df], axis=1)

    # remove the duplicates 
    df.drop_duplicates(inplace=True)

    return df


def export_sql(df, table_name):

    engine = create_engine(f'sqlite:///{table_name}.db')
    try:
        df.to_sql('messages_categories', engine, index=False)
    except Exception as e:
        print('Warning: Database already exist')
    else:
      print("SUCCESS: SQL file exported")


def main(MESSAGE_DF_PATH, CAT_DF_PATH):

    print('MESSAGE: Step 1 Load dataSets')
    message_df, categories_df = load_data(MESSAGE_DF_PATH, CAT_DF_PATH)       
         

    print('MESSAGE: Step 2 Merge the datasets on `id`')
    df = merge_datesets(message_df, categories_df)

    print('MESSAGE: Step 3 Category column transfomation')
    cat_df = transform_category_col(df.categories)

    print('MESSAGE: Step 4 Add cat_df to df and drop cat col')
    df = df_transform(df, cat_df)

    print('MESSAGE: Step 5 Export to sql')
    export_sql(df, 'messages_categories')

    print('SUCCESS: Data Wrangling Done')
    return df


if __name__ == '__main__':
    if len(sys.argv) == 3:

        MESSAGE_DF_PATH, CAT_DF_PATH = sys.argv[1:]

        main(MESSAGE_DF_PATH, CAT_DF_PATH) 

    else: 
        print(""" ERROR: Please provide the filepaths of the messages and categories 
            datasets as the first and second argument respectively """)
