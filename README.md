# Acquire data from different sources
Extract data from different sources(web pages, JSON files, text files etc.)

## Introduction
Acquire data from different sources and store it different database platforms and files.

## Tasks
1. Scrape data from web-pages, find patterns in the data and store it in MySQL.

## Technologies used
MySQL Workbench

Python(mysql.connector, requests, bs4 and re libraries)

## Setup
1. Pick a web page to scrape and insert the address in the 'data_acquisition.py' file near the end of the file in the function 'call_functions()' across the variable name 'web_page'.
2. Create list of lists. Each inner list should contain two values: the regular expression('re.') pattern and a name for the pattern. These names will become MySQL column names. This is how the list of lists should look like: patterns = [['£\d', '£d'], ['£\d\d', '£dd'], ['£\d\d\d', '£ddd'],['£', '£']]
