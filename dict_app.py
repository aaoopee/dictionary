
import json

data = json.load(open("data/data.json"))

word = input("Word: ")

print(data[word])