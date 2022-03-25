import requests
import json

file = open('file.json','w+')

response = requests.get("https://api.thedogapi.com/v1/breeds")
print(response.text)

jsIn = response.text
py = json.loads(jsIn)
js = json.dumps(py,indent=4)

file.write(js)
file.close()
