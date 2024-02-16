import pandas as pd 

def json_to_csv(json_file, csv_file):
    data = pd.read_json(json_file)
    data.to_csv(csv_file, index=False)

json_to_csv('MurilloJson.json', 'arquivo.csv')