from autoviz import AutoViz_Class
import os

BASE_DIR_PATH = '/Users/neilb/Documents/dsci_thesis/'
DATA_PATH = 'Scraping_and_Cleaning'

DATASET_FILE = os.path.join(BASE_DIR_PATH, DATA_PATH, 'data_2022.csv')

AV = AutoViz_Class()

profile = AV.AutoViz(DATASET_FILE, chart_format='server')