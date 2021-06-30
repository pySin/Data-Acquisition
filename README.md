# Acquire data from different sources
Extract data from different sources(web pages, JSON files, text files etc.)

## Introduction
Acquire data from different sources and store it in different database platforms and files.

## Tasks
1. Scrape data from web-pages, find patterns in the data and store it in MySQL.
2. Combine the text from the .docx files in a folder and put them in 1 .docx document.

## Technologies used
MySQL Workbench

Python(mysql.connector, requests, bs4, docx and re libraries)

## Setup
### Task 1
1. Pick a web page to scrape and insert the address in the 'data_acquisition.py' file near the end of the file in the function 'call_functions()' across the variable name 'web_page'.
2. Pick an HTML tag to look for in the web-scraped object and assign it to the 'tag' variable in the 'call_functions()' function.
3. Create list of lists. Each inner list should contain two values: the regular expression('re.') pattern and a name for the pattern. These names will become MySQL column names. This is how the list of lists should look like: patterns = [['£\d', '£d'], ['£\d\d', '£dd'], ['£\d\d\d', '£ddd'],['£', '£']]
4. Pick a database name and a table name from the MySQL server to insert the pattern data acquired. Insert those instead of 'database_1' and 'table_2' in the following row: `transfer_o = transfer('database_1', 'table_2', data_dict)`.
5. Use your hostname, username and password to connect python with MySQL using mysql.connector`conn = mysql.connector.connect(user='root', host='localhost', password='dance')`
