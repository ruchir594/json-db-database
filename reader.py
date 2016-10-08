import json
import csv

with open('template.csv', 'rb') as f:
    fp = csv.reader(f, delimiter=',')
    for row in fp:
        print row
