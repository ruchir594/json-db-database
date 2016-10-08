import json
import csv

csv_file_name = 'template.csv'

def get_columns():
    with open('template.csv', 'rb') as f:
        fp = csv.reader(f, delimiter=',')
        column_names = []
        column_type = []
        for row in fp:
            if len(row) == 2:
                column_names.append(row[0])
                column_type.append(row[1])
            else:
                print 'Error with ' + csv_file_name
        return column_names, column_type
    return [], []
