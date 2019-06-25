import ast

import requests
import pandas as pd

from pandas.io.json import json_normalize

import json

# import_from_the_web est censé retourner une valeur?
# suggestion: soit faire en sorte qu'import_from_the_web recuperer les donnees et l ecrive sous un ficher
# en plus de la retourner, soit faire qu'import_from_the_web ne la retourne pas, et appeler
# inconditionellement import_from_csv apres avoir appele import_from_the_web (probablement apres avoir renomme 
# import_from_the_web en fetch_data ou qqch comme ca)
def import_from_the_web(start_date, end_date):
    r = requests.get(
        'https://api.exchangeratesapi.io/history?start_at=' + start_date + '&end_at=' + end_date)
    data = (r.json())
    print(data)
    df = pd.DataFrame.from_records(data["rates"]).T
    print(df)
    df.to_csv('./data/from' + start_date +
              '_to_' + end_date + '_formatted.csv')


def import_from_csv(start_date, end_date):
    return pd.read_csv('./data/from' + start_date +
                       '_to_' + end_date + '_formatted.csv', index_col=0)
