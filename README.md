# dsci_thesis

* page_interact.py and scrape.py contains the main functions used for the scraping process
* The previous main.py has been separated into rainfall_scraping.py and waterlevel_scraping.py, which contains the scraping loop
* Inputs to be changed are same as before
* 27-28s for a days worth of water level data; ~6mins for a days worth of rainfall data; plan accordingly
* merge.py only when everything is finished
* Do not download csv files, they contain 2022 data and the script will not erase this data when writing to the csv file
* No need to create csv file manually, code will do it for you
