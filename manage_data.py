import json
import time

from reader import get_columns

def init_json(file, db_name):
    data = {"db_name": db_name, "rows":[]}
    with open(file, 'w') as outfile:
        json.dump(data, outfile)

def get_element(file, id):
    with open(file, 'r') as f:
         data = json.load(f)
    flag = False
    for i in data["rows"]:
        if i["id"] == id:
            flag = True
            with open(file, 'w') as f:
                 json.dump(data, f)
            return i
    flag = False
    if flag == False:
        columns = get_columns()
        column_names = columns[0]
        column_type = columns[1]
        # column_subsitude will help build the string which will help initialize each row
        column_subsitude = []
        for each_column in column_type:
            if each_column.lower() == 'string':
                column_subsitude.append('""')
            elif each_column.lower() == 'number':
                column_subsitude.append('-1')
            elif each_column.lower() == 'bool':
                column_subsitude.append('"False"')
            elif each_column.lower() == 'array':
                column_subsitude.append('[]')
        # json_string_element is the string we will build, which will later be converted into
        # JSON object
        json_string_element = '{"id":'+id+','
        i=0
        for i in range(len(column_names)):
            json_string_element = json_string_element + '"' + column_names[i] + '": ' + column_subsitude[i] + ','
        json_string_element = json_string_element[:-1] #to remove the last extra ','
        json_string_element = json_string_element + '}'
        # Now we have a fully initialized JSON string
        killbill = json.loads(json_string_element)
        data["rows"].append(killbill)
        with open(file, 'w') as f:
             json.dump(data, f)
        return killbill

def update_element(file, element):
    with open(file, 'r') as f:
         data = json.load(f)
    for i in data['rows']:
        if i['id'] == element['id']:
            i['intent'] = element['intent']
            i['intent_to'] = element['intent_to']
            i['intent_type'] = element['intent_type']
            i['show'] = element['show']
            i['venue'] = element['venue']
            i['location'] = element['location']
            i['time'] = element['time']
            i['day'] = element['day']
            i['response_type'] = element['response_type']
            i['number_of_tickets'] = element['number_of_tickets']
            i['timestamp'] = int(round(time.time() * 1000))
            break
    with open(file, 'w') as f:
         json.dump(data, f)

def wash_element(file, element):
    with open(file, 'r') as f:
         data = json.load(f)
    for i in data['rows']:
        if i['id'] == element['id']:
            i['intent'] = 'washed'
            i['intent_to'] = ''
            i['intent_type'] = ''
            i['show'] = ''
            i['venue'] = ''
            i['location'] = ''
            i['time'] = ''
            i['day'] = ''
            i['number_of_tickets'] = 1
            i['timestamp'] = int(round(time.time() * 1000))
            break
    with open(file, 'w') as f:
         json.dump(data, f)

#init_json('data.json', 'trial')
get_element('data.json','104')
