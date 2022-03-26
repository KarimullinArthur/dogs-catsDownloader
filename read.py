#!/bin/python3

import json

what = input('1)Dog\n2)Cat\n[1/2]? ')

if what == '1':
    what = 'dog'

elif what == '2':
    what = 'cat'
try:
    file =  open(f'{what}.json')
    
    py = json.load(file)
    
    items = len(py)
    
    max_indent = len(max(py, key=len)) + 1
    
    for i in range(0,items):
        print(py[i]['life_span'],'\t',py[i]['name'])

except FileNotFoundError:
    print('First run load.py')
