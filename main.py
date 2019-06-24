import sys

import time
from datetime import datetime

from src import data_preprocess
from src import luminx

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Import financial data and generate a LED program.')

    parser.add_argument('--fromweb',
                        action="store_true",
                        help="If you want to import new data from the web.")
    parser.add_argument('--fromcsv',
                        action="store_true",
                        help="If you want to use data already imported in a CSV.")
    parser.add_argument('--yesgif',
                        action="store_true",
                        help="If you want to generate a gif with the data.")
    parser.add_argument('-s', type=str,
                        dest='start_day',
                        help="The first day of the imported time series.")
    parser.add_argument('-e', type=str,
                        dest='end_day',
                        help="The last day of the imported time series.")
    parser.add_argument('-n', type=str,
                        dest='name_movie',
                        help="The name of the gif that will be generated.")

    args = parser.parse_args()

    if args.fromweb:
        pure_data = data_preprocess.import_from_the_web(
            args.start_day, args.end_day)
    elif args.fromcsv:
        pure_data = data_preprocess.import_from_csv(
            args.start_day, args.end_day)
    else:
        print('Valid modes are: --fromweb and --fromcsv. Try again !')
        sys.exit("Error: No valid mode was given.")

    if args.yesgif:
        (red_df, blue_df) = luminx.from_formatted_to_colours(pure_data)
        luminx.from_colours_to_screen(
            red_df, blue_df, args.name_movie, size_led=20, space_led=3)
        print("A gif has been generated !")
    else:
        print('No gif is being generated.')

    print("Code executed.")
