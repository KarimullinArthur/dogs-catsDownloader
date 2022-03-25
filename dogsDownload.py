import json
import os
import random

file =  open('file.json')

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
os.system(f"mv ./img/{id}.jpg ./img/{name}.jpg") 
print('Done!')
file.close()
