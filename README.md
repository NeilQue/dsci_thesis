# dsci_thesis

## Files and Instructions
* page_interact.py and scrape.py contains the main functions used for the scraping process
* The previous main.py has been separated into rainfall_scraping.py and waterlevel_scraping.py, which contains the scraping loop
* Inputs to be changed are same as before
* 27-28s for a days worth of water level data; ~6mins for a days worth of rainfall data; plan accordingly
* merge.py only when everything is finished
* Do not download csv files, they contain 2022 data and the script will not erase this data when writing to the csv file
* No need to create csv file manually, code will do it for you
* checks.py not important

## Errors
* TimeoutException: napagod yung program maghintay sa loading ng page; ito pinakamalaking chance mangyare pero normal lang yan
* ElementClickInterceptedException: di maclick yung button kasi may nakaharang
* StaleElementReferenceException: natagalan sa pagload ng data, kala ko di na lalabas to ulit
* When error/exeption occurs, program shows you the datetime it ended, continue scrape from there
  * check file para sure kung ano kelangan start na datetime
* all cases run lang ulit ng code, pretty sure di na kelangan ng code changes (unless konti palang talaga nag eerror na ulit)

## To Do:
* [not urgent: mas tatagal pa ata pag inaral ko pa to] try to lessen scraping time using pandas 2.0 and pyarrow
  * https://towardsdatascience.com/pandas-2-0-a-game-changer-for-data-scientists-3cd281fcc4b4
  * https://airbyte.com/blog/pandas-2-0-ecosystem-arrow-polars-duckdb
* EDA using jupyter and pygwalker for no-code data viz; maybe R for stuff that involves calculations for precision of decimal arithmetic
  * https://github.com/Kanaries/pygwalker

## PAGASA Website
* http://121.58.193.173:8080/rainfall/table.do
* http://121.58.193.173:8080/water/table.do
