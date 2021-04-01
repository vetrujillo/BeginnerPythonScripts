import json

filename = 'fav_number.txt'

with open(filename) as file_object:
    fav_number = json.load(file_object)

print("I know your favorite number! It is " + fav_number)