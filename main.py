
import sys

import time
from datetime import datetime

from src import data_preprocess
from src import luminx

if __name__ == "__main__":
    # execute only if run as a script
    current_time = datetime.now().strftime("%Y_%M_%D_%h_%m_%s")
    mode = sys.argv[1]
    gif = sys.argv[2]

    if mode == '-fromweb':
        pure_data = data_preprocess.import_from_the_web(
            '2019-06-17', '2019-06-19')
    elif (mode == '-fromcsv'):
        pure_data = data_preprocess.import_from_csv()
    else:
        print('Valid modes are: -fromweb and -fromcsv. Try again !')

    if (gif == '-yesgif'):
        pure_colours = luminx.from_formatted_to_colours(pure_data)
        luminx.from_colours_to_screen(pure_colours, 'my_movie')
        print("A gif has been generated !")
    else:
        print('No gif is being generated.')

    print("Code executed.")
