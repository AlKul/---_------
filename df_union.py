import pandas as pd
import os
from os.path import isfile, join

def df_union():
    mypath = './pickle_files'
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

    print(onlyfiles)

    df = pd.DataFrame()
    for file in onlyfiles:
        df_cur = pd.read_pickle(os.path.join(mypath, file))
        print(f"Read {df_cur.shape[0]}")
        df = pd.concat([df, df_cur], ignore_index=True)
    df.to_pickle(f'./pickle_files/All_companies.pkl')
    df.to_csv(f'./csv_files/All_companies.csv')


print('Df union')
