import json

# Sample JSON data
json_data = '''
[
  {
    "name": "John",
    "age": 30,
    "city": "New York",
    "salary": 20000
  },
  {
    "name": "Jane",
    "age": 25,
    "city": "San Francisco"
  }
]
'''

# Parse the JSON data
data = json.loads(json_data)

# Loop through the array of objects
for item in data:
    message = f"Name: {item['name']} Age: {item['age']}"
    print(message)

keys = ['name', 'age', 'salary']


def get_value(key, item):
    if key in item:
        result = item[key]
    else:
        result = None
    return result


def print_data(data):
    for item in data:
        message = []
        for k in keys:
            message.append(get_value(k, item))
        print(message)


# Read the JSON data from a file
with open("resources/sample.json", "r") as f:
    data = json.load(f)
