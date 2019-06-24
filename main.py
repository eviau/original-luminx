import sys

import time
from datetime import datetime

from src import data_preprocess
from src import luminx

import argparse

if __name__ == "__main__":

    # ici tu peux utiliser argparse pour lire les arguments: https://docs.python.org/3/library/argparse.html

    parser = argparse.ArgumentParser(description='Import financial data and generate a LED program.')

    parser.add_argument('--fromweb',
                    action="store_true")
    parser.add_argument('--fromcsv',
                    action="store_true")
    parser.add_argument('--yesgif',
                    action="store_true")
    parser.add_argument('-s', type=str, dest='start_day')
    parser.add_argument('-e', type=str, dest='end_day')
    parser.add_argument('-n',type=str, dest='name_movie')

    args = parser.parse_args()

    if args.fromweb:
        pure_data = data_preprocess.import_from_the_web(
            args.start_day, args.end_day)
    elif args.fromcsv:
        pure_data = data_preprocess.import_from_csv(args.start_day, args.end_day)
    else:
        print('Valid modes are: -fromweb and -fromcsv. Try again !')
        # bug ici: il faut quitter la fonction! 
        # tu peux utiliser sys.exit pour quitter le script entierement
        # la convention sous Unix est de retourner un code d'erreur different de 0 quand le programme
        # s'arrete avec une erreur, et 0 si tout va bien. Python va retourner 0 automatiquement.
        # https://docs.python.org/3/library/argparse.html
    if args.yesgif:
        (red_df, blue_df) = luminx.from_formatted_to_colours(pure_data)
        luminx.from_colours_to_screen(
            red_df, blue_df, args.name_movie, size_led=20, space_led=3)
        print("A gif has been generated !")
    else:
        print('No gif is being generated.')

    print("Code executed.")
