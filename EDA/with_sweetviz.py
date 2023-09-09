import sweetviz as sv
import pandas as pd
import os

BASE_DIR_PATH = '/Users/neilb/Documents/dsci_thesis/'
DATA_PATH = 'Scraping_and_Cleaning'

DATASET_FILE = os.path.join(BASE_DIR_PATH, DATA_PATH, 'data_2022.csv')

df = pd.read_csv(DATASET_FILE, engine='pyarrow')

report = sv.analyze(df)
report.show_html()