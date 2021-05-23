# Data acquisition 2

import requests
from bs4 import BeautifulSoup
import re
import mysql.connector


class acquisition:

    def __init__(self):
        pass

    # Get the content of a web page.
    def scrape(self, web_page):

        # Get the content of the web page with requests library.
        content = requests.get(web_page)

        # Create BeautifulSoup object with the content.
        soup = BeautifulSoup(content.text, 'lxml')
        return soup

    # Find the usefull data from the web page.
    def find_data(self, soup, tag, patterns):

        # Specify the HTML tag of interest.
        content = soup.find_all(tag)

        # Create dictionary for patterns and their results.
        col_name_values = {}

        # Look for patterns.
        for pattern in patterns:

            # Make a list to save all the pattern matches found.
            data_list = []

            # Search trough the text for pattern matches and append
            # them to the data list.
            for item in content:
                matches = re.findall(pattern[0], item.text)
                if matches:
                    data_list.append(matches)

            # Merge the lists from all tags discovered(stoerd in 'data_list')
            merged_list = []
            for item in data_list:
                for inner_item in item:
                    merged_list.append(inner_item)

            # Create dictionary entry for each merged list.
            col_name_values[pattern[1]] = merged_list

        return col_name_values


# Transfer data to MySQL.
class transfer:

    # Initialize object.
    def __init__(self, database, table, data_dict):
        self.database = database
        self.table = table
        self.data_dict = data_dict

    # Create table for web-page acquired data.
    def create_table(self):

        columns_string = ''

        # Create sub-query for the main MySQL query.
        for item in self.data_dict:
            columns_string = columns_string+str(item)+' VARCHAR(255), '

        columns_string = columns_string[:-2]

        # Main query.
        query = '''
            CREATE TABLE IF NOT EXISTS %s.%s(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            %s);
                ''' % (self.database, self.table, columns_string)

        # Send the query to MySQL.
        conn = mysql.connector.connect(user='root', host='localhost',
                                       password='dance')  # MySQL connection.
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

    # Populate the newly created table with the scraped data.
    def populate_table(self):

        column_names = ''

        # Create the column names string.
        for item in self.data_dict:
            column_names = column_names+str(item)+', '
        column_names = column_names[:-2]

        ## Create the columns values string.

        # Find the longest list first.
        lengths = []

        for length in self.data_dict:
            lengths.append(len(self.data_dict[length]))

        # Create the value data rows one by one and add them together.
        insert_values = ''

        for len_i in range(max(lengths)):
            insert_line = ''
            for item_d in self.data_dict:
                try:
                    insert_line = insert_line+'\''+self.data_dict[item_d]\
                                  [len_i]+'\''+', '
                except Exception:
                    insert_line = insert_line+'NULL, '

            insert_values = insert_values+'('+insert_line[:-2]+'),'+'\n'

        insert_values = insert_values[:-2]

        # Assemble the main query.
        query = '''
            INSERT INTO %s.%s(%s)
            VALUES%s;
                ''' % (self.database, self.table, column_names, insert_values)

        # Send the query to MySQL.
        conn = mysql.connector.connect(user='root', host='localhost',
                                       password='dance')  # MySQL connection.
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()


# Call the necessary functions.
def call_functions():
    data_acq = acquisition()
    web_page = 'https://www.ebay.co.uk/?mkcid=1&mkrid=710-53481-19255-\
                0&siteid=3&campid=5337314663&customid=&toolid=10001&mkevt=1'
    b_soup = data_acq.scrape(web_page)
    tag = 'div'
    # Along with the patterns, their labels are added as well.
    patterns = [['£\d', '£d'], ['£\d\d', '£dd'], ['£\d\d\d', '£ddd'],
                ['£', '£']]
    data_dict = data_acq.find_data(b_soup, tag, patterns)
    transfer_o = transfer('database_1', 'table_2', data_dict)
    transfer_o.create_table()
    transfer_o.populate_table()


# Call the script.
if __name__ == '__main__':
    call_functions()
