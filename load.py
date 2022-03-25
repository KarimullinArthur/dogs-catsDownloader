import requests
import json

dog = requests.get("https://api.thedogapi.com/v1/breeds")
cat = requests.get("https://api.thecatapi.com/v1/breeds")

what = input("1)Dogs\n2)Cats")
if what == '1':
    file = open('dogs.json','w+')
    print(dog.text)
    jsIn = dog.text
if what == '2':
    file = open('cats.json','w+')
    print(cat.text)
    jsIn = cat.text

py = json.loads(jsIn)
js = json.dumps(py,indent=4)

file.write(js)
file.close()
