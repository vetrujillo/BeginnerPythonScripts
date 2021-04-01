filenames = ['cats.txt', 'dogs.txt', 'other.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        pass