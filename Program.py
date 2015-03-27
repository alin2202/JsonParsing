# REQUIREMENTS:
# Write a program in python that will parse the given testdata and output the following on the screen
#     - A list of all organs with a "central" attribute
#     - A dictionary of key-value pair of all the "things in my head"
#     - An ordered (by alpha) sort of all items at the upper level

__author__ = 'Alina'

import sys
import Functions as fn

# Create a variable for file name
file = ''

# Assign a name for test file if file name s provided
# or throw the error message if there is no argument
try:
    file = sys.argv[1]
except:
    print('ERROR: No file name provided. Please provide valid file name/path'
          '\nExample usage: Program.py file_to_parse.txt')

# Parse file to json object
json_obj = fn.parse_json (file)

# Select and print list of organs with value "central"
fn.select_objects_by_value(json_obj, 'organs', 'central')

# Select and print a dictionary of key-value pair of
# things in my head
fn.select_objects_by_name(json_obj, 'things in my head')

# Select upper level items and print them ordered (by alpha)
fn.order_top_level_objects(json_obj)