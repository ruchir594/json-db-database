import json
import csv

csv_file_name = 'template.csv'
json_file_name = 'template.json'

class ExcessColumns(Exception):
    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return repr(self.arg)

def get_columns():
    column_names = []
    column_type = []
    with open(json_file_name) as json_data:
        d = json.load(json_data)
        fp = d['columns']
        for row in fp:
            if len(row) == 2:
                column_names.append(row[0])
                column_type.append(row[1])
            else:
                raise ExcessColumns("in the file " + csv_file_name)
    return column_names, column_type

#print get_columns()

'''def get_columns():
    column_names = []
    column_type = []
    with open(csv_file_name, 'rb') as f:
        fp = csv.reader(f, delimiter=',')
        for row in fp:
            if len(row) == 2:
                column_names.append(row[0])
                column_type.append(row[1])
            else:
                raise ExcessColumns("in the file " + csv_file_name)
    return column_names, column_type'''
