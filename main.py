## ici tu peux ajouter le shebang python3: https://stackoverflow.com/questions/7670303/purpose-of-usr-bin-python3/7670338
import sys

import time
from datetime import datetime

from src import data_preprocess
from src import luminx

### a faire: regler VS code pour utiliser le formatage PEP8 automatique a la sauvegarde 

if __name__ == "__main__":
    # execute only if run as a script
    current_time = datetime.now().strftime("%Y_%M_%D_%h_%m_%s")
    
    # ici tu peux utiliser argparse pour lire les arguments: https://docs.python.org/3/library/argparse.html
    mode = sys.argv[1]
    gif = sys.argv[2]
    start_day = sys.argv[3]
    end_day = sys.argv[4]
    name_movie = sys.argv[5]

    if mode == '-fromweb':
        pure_data = data_preprocess.import_from_the_web(
            start_day, end_day)
    elif (mode == '-fromcsv'):
        pure_data = data_preprocess.import_from_csv(start_day, end_day)
    else:
        print('Valid modes are: -fromweb and -fromcsv. Try again !')
        # bug ici: il faut quitter la fonction! 
        # tu peux utiliser sys.exit pour quitter le script entierement
        # la convention sous Unix est de retourner un code d'erreur different de 0 quand le programme
        # s'arrete avec une erreur, et 0 si tout va bien. Python va retourner 0 automatiquement.
        # https://docs.python.org/3/library/argparse.html
    if (gif == '-yesgif'):
        (red_df, blue_df) = luminx.from_formatted_to_colours(pure_data)
        luminx.from_colours_to_screen(red_df, blue_df, name_movie,size_led = 20 , space_led = 3)
        print("A gif has been generated !")
    else:
        print('No gif is being generated.')

    print("Code executed.")
