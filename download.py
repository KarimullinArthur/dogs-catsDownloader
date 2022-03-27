#!/bin/python3

import json
import os
import random
import sys

what = input('1)Dog\n2)Cat\n[1/2]? ')

if what == '1':
    what = 'dog'

elif what == '2':
    what = 'cat'

else:
    sys.exit('What?\nI said 1 or 2!')

try:
    file =  open(f'./json/{what}.json')


except FileNotFoundError:
    sys.exit("First run load.py")

py = json.load(file)
    
index = random.randint(0,len(py)-1)
print('Chose a random dog')
   
url = py[index]['image']['url']
id = py[index]['image']['id']
name = py[index]['name']
print(f'She/Her name is {name}')
 
sym = [' ','_','(',')']
 
for j in sym:
    name = name.replace(j,'-')
 
print('Downloading...')
os.system(f"wget {url} -P ./img/ >/dev/null 2>&1")
os.system(f"mv ./img/{id}.jpg ./img/{name}.jpg >/dev/null 2>&1") 
print('Done!')
file.close()
