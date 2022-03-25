import json

file =  open('file.json')

py = json.load(file)

items = len(py)

max_indent = len(max(py, key=len)) + 1

for i in range(0,items):
    print(py[i]['life_span'],'\t',py[i]['name'])
