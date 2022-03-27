#!/bin/python3

import requests
import json
import os
import sys

urlDog = "https://api.thedogapi.com/v1/breeds"
urlCat = "https://api.thecatapi.com/v1/breeds"

what = input("1)Dogs\n2)Cats\n[1/2]? ")
if what == '1':
    what = 'dog'
    dog = requests.get(urlDog)
    jsIn = dog.text

elif what == '2':
    what = 'cat'
    cat = requests.get(urlCat)
    jsIn = cat.text

else:
    sys.exit('What?\nI said 1 or 2!')

os.system('mkdir ./json >/dev/null 2>&1')
with open(f'./json/{what}.json','w+') as file:
    py = json.loads(jsIn)
    js = json.dumps(py,indent=4)
    
    file.write(js)
    print('Done!') 
