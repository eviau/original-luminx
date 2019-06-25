import pandas as pd

from PIL import Image
import numpy as np

import imageio


def translate_format_range(x, input_low, input_high, output_low, output_high):
    df = ((x - input_low) / (input_high - input_low)) * \
        (output_high - output_low) + output_low
    df.fillna(0, inplace=True)
    df.round(2)
    return df


def from_formatted_to_colours(df):
    df.fillna(0, inplace=True)
    df = df.sort_index().pct_change()
    df.fillna(0, inplace=True)
    # sauvegarder df < 0 et df >= 0 dans une variable intermediaire
    red_df = translate_format_range(
        df[df < 0], df[df < 0].min(), df[df < 0].max(), 0.0, 255.0)
    blue_df = translate_format_range(
        df[df >= 0], df[df >= 0].min(), df[df >= 0].max(), 0.0, 255.0)
    return (red_df, blue_df)


def from_colours_to_screen(red_df, blue_df, name, size_led, space_led):
    # pourquoi space * 2?
    width_strip = red_df.columns.shape[0]*(space_led*2+size_led)
    height_strip = size_led + space_led*2
    # pourquoi 3 ?
    data = np.zeros((height_strip, width_strip, 3), dtype=np.uint8)
    n = space_led
    frames = []
    
    # que represente n?
    for m in range(0, red_df.shape[0]):
        for col in red_df.columns:
            data[space_led:(size_led+space_led), n:(n+size_led)
                 ] = [red_df[col][m], 0, blue_df[col][m]]
            n = n + space_led*2 + size_led
        img = Image.fromarray(data, 'RGB')
        frames.append(img)
        n = space_led
    imageio.mimsave(name + '.gif', frames)
