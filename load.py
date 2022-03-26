#!/bin/python3

import requests
import json

dog = requests.get("https://api.thedogapi.com/v1/breeds")
cat = requests.get("https://api.thecatapi.com/v1/breeds")

what = input("1)Dogs\n2)Cats\n[1/2]? ")
if what == '1':
    what = 'dog'
    jsIn = dog.text

elif what == '2':
    what = 'cat'
    jsIn = cat.text

file = open(f'{what}.json','w+')

py = json.loads(jsIn)
js = json.dumps(py,indent=4)

file.write(js)
print('Done!')
file.close()
