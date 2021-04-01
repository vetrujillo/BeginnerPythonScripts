import json

filename = 'fav_number.txt'

try:
    with open(filename) as file_object:
        fav_number = json.load(file_object)
        print("I know your favorite number! It is " + fav_number)
        
except FileNotFoundError:
    print("No entry located. Prompting user now...")
    fav_number = input("Please enter your favorite number: ")
    with open(filename, 'w') as file_object:
        json.dump(fav_number, file_object)

