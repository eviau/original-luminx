import ast

import requests
import pandas as pd

from pandas.io.json import json_normalize

import json

def import_from_the_web(start_date, end_date):
    # r = requests.get(
    #     'https://api.exchangeratesapi.io/history?start_at=' + start_date + '&end_at=' + end_date)
    # data = (r.json())
    # data2  = json.loads(r.text)
    # print(data)
    # print(data2)
    # df = pd.DataFrame.from_records(data) 
    # print(df)
    df = pd.read_csv('temp_from_the_web.csv')

    # print(print(data.keys()))
    df2 = (pd.io.json.json_normalize(df,record_path='rates') )

    # df2.columns = df2.columns.map(lambda x: x.split(".")[-1])
    print(df2)
    df_new = format_data(df)
    df_new.to_csv('../data/from' + start_date + ' _to_'  + end_date + '_formatted.csv')


def only_dict(d):
    '''
    Convert json string representation of dictionary to a python dict
    '''
    return  pd.io.json.json_normalize(d) 


def format_data(df):
    #df_new = json_normalize(df.apply(only_dict).tolist())
    print(df.columns)
    print(df.index)
    df.reset_index()
    print(df.rates)
    print(df_new = json_normalize(df,record_path=['rates'],meta=[['rates']]))
    print( pd.DataFrame.from_records(df.rates))
    df_new = df.rates.apply(only_dict).tolist()
    # 
    return df_new

def import_from_csv():
    return pd.read_csv('data/from1999_to_2019june_formatted.csv')