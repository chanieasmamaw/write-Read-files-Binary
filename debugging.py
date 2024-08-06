"""

import json
data = {
	"name": "Alice",
	"age": 25,
	"is student": True,
	"course": ["Englis","History"]
}

with open('data.json', 'w') as file:
	json.dump(data, file)
with open('data.json', 'r' ) as file:
	data = json.load(file)
data['age'] = 21
with open('data.json', 'w') as file:
	json.dump(data, file, indent=4)
print(data)
print(type(data))

"""

with open()