# class contains following methods:
# - parse_json (file_name)
# - select_objects_by_value (data, item_name, item_value)
# - select_objects_by_name (data, item_name)
# - order_top_level_objects (data)

__author__ = 'Alina'

import json
import re

# function to parse existing file
def parse_json (file_name):
    # read file to a list of lines
    file_data = open(file_name).readlines()
    # create variable for parsed json data string
    json_data = ""
    # go through file lies and for each line:
    for line in file_data:
        # search for "<Warning"> in line
        line_obj = re.search("<Warning>", line)
        if line_obj:
            # ignore lines that have
            # searched patern
            continue
        else:
            # replace "None" values to "0"
            line = re.sub("None", "0", line)
            # append line to json_data string
            json_data += line
    # parse json string to json object
    extracted_json_data = json.loads(json_data)
    # return parsed data
    return extracted_json_data

# function that prints data key based on it's value
def select_objects_by_value (data, item_name, item_value):
    objects = []
    for item in data[item_name]:
        for thing in item:
            name = item.get(thing)
            if name == item_value:
                objects.append(thing)
    print('\n1) A list of all organs with a "central" attribute')
    print(objects)

# function that prints key-value pairs for selected object
def select_objects_by_name (data, item_name):
    print('\n2) A dictionary of key-value pair of all the "things in my head" ')
    print(data[item_name])

# function prints ordered (by alpha) sort of all items at the upper level
def order_top_level_objects (data):
    objects = []
    for item in data:
        objects.append(item)
    objects.sort()
    print('\n3) A sorted list of upper level items:')
    print(objects)