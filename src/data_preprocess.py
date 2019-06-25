import json
import pandas as pd
from pandas.io.json import json_normalize
import requests


def import_from_the_web(start_date, end_date):
    r = requests.get(
        'https://api.exchangeratesapi.io/history?start_at=' + start_date + '&end_at=' + end_date)
    data = (r.json())
    df = pd.DataFrame.from_records(data["rates"]).T
    df.to_csv('./data/from' + start_date +
              '_to_' + end_date + '_formatted.csv')
    return df


def import_from_csv(start_date, end_date):
    return pd.read_csv('./data/from' + start_date +
                       '_to_' + end_date + '_formatted.csv', index_col=0)
