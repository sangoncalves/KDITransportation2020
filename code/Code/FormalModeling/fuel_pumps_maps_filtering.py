'''
This file parse the accomodation dataset and filter
the needed information based on the schema.

@carbogninalberto
'''
import pandas as pd

if __name__ == "__main__":
    pd.options.mode.chained_assignment = None
    print("1. Loading CSV file into a pandas dataframe")
    # loading the elaborated dataset from previous phase
    dataset_path = '../../dataset/Scope Definition & Inception/data/fuel_pumps_maps/Mappa-dei-distributori-di-carburante-in-italia.csv'
    dataset = pd.read_csv(dataset_path, sep=";", encoding="ISO-8859-1", error_bad_lines=False, warn_bad_lines=False)

    # filtering
    filtered_dataset = dataset[['Longitudine', 'Latitudine', 'Comune', 'Provincia', 'Regione', 'Nome']]
    filtered_dataset.rename(columns={
        'Longitudine': 'Longitude', 
        'Latitudine': 'Latitude',
        'Comune': 'City',
        'Provincia': 'Province',
        'Regione': 'Region',
        'Nome': 'Name'
    }, inplace=True)
    filtered_dataset.to_json('../../dataset/Formal Modeling/data/fuel_pumps.json', orient='records', lines=False)

    