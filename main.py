
import requests
import pprint
import json

from pandas.io.json import json_normalize

import ast

import pandas as pd
from pandas.compat import StringIO

from PIL import Image
import numpy as np

import imageio


def import_from_the_web():
    r = requests.get(
        'https://api.exchangeratesapi.io/history?start_at=1999-01-01&end_at=2019-06-10')
    data = (r.json())
    df = pd.DataFrame.from_records(data)
    print(df)
    df.to_csv('from1999_to_2019june.csv')


def only_dict(d):
    '''
    Convert json string representation of dictionary to a python dict
    '''
    return ast.literal_eval(d)


def format_data():
    df = pd.read_csv('from1999_to_2019june.csv')

    a = json_normalize(df['rates'].apply(only_dict).tolist())
    print(a)

    df_new = df[['day_id', 'rates']].groupby('day_id', sort=True).rates.apply(
        lambda x: json_normalize(x.apply(only_dict).tolist()))

    print(df_new.head(10))

    df_new.to_csv('from1999_to_2019june_formatted.csv')


def from_formatted_to_colours():
    df = pd.read_csv('from1999_to_2019june_formatted.csv')
    df.fillna(0, inplace=True)
    actual_data = df
    actual_data.set_index(pd.to_datetime(
        actual_data.day_id, yearfirst=True), inplace=True)
    actual_data.drop(['day_id'], axis=1, inplace=True)
    act_dat = actual_data.sort_index().pct_change()
    act_dat.fillna(0, inplace=True)
    data_pct = act_dat
    data_pct[data_pct >= 0] = (((data_pct[data_pct >= 0] - data_pct.min()) *
                                ((255 - 127)/(data_pct.max() - 0)))+127)
    data_pct[data_pct < 0] = (((data_pct[data_pct < 0] - data_pct.min()) *
                               ((127 - 0)/(0 - data_pct.min()))))
    data_pct.reset_index(inplace=True)
    data_pct.drop(['day_id'], axis=1, inplace=True)

    data_pct.round(2)
    data_pct.to_csv("final_data_rwb_final.txt", float_format='%.f',
                    index=False, header=False)


def from_colours_to_screen():
    df = pd.read_csv("final_data_rwb_final.txt")
    print(df.head(5))

    w, h = (41*6+41*10), (16)
    data = np.zeros((h, w, 3), dtype=np.uint8)
    n = 3
    frames = []
    for m in range(0, df.shape[0]):
        for col in df.columns:
            data[3:13, n:(n+10)] = [df[col][m], 0, 0]
            n = n + 16
        img = Image.fromarray(data, 'RGB')
        frames.append(img)
        n = 3
    imageio.mimsave('movie.gif', frames)


if __name__ == "__main__":
    # execute only if run as a script
    from_colours_to_screen()
    print("Code executed.")
