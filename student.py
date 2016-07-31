import json

with open("student.json") as json_file:
    json_data = json.load(json_file)
    input("Plz Enter your ID Number:")
    print(json_data)