filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print("\n")

with open(filename) as file_object:
    lines = file_object.readlines()
    list = []
    for line in lines:
        print(line.rstrip())
        list.append(line)

print("\n")

for item in list:
    print(item.rstrip())
