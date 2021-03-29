filename = 'guest_book.txt'

prompt = "\nPlease enter your name: "
prompt += "\nType 'q' when finished. "

while True:
    name = input(prompt)
    if name == 'q':
        break
    else:
        print("Welcome, " + name + "!")
        print("\nAdding name to guestbook...\nDone!")
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")