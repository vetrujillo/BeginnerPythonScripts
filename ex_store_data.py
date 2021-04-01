import json

filename = 'fav_number.txt'
fav_number = input("Please enter your favorite number: ")

with open(filename, 'w') as file_object:
    json.dump(fav_number, file_object)

