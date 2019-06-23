import pandas as pd

from PIL import Image
import numpy as np

import imageio


def from_formatted_to_colours(df):
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
    return data_pct


def from_colours_to_screen(df,name):
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
    imageio.mimsave(name + '.gif', frames)