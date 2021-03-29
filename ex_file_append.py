from random import randint

filename = 'programming_poll.txt'

prompt = "\nWhat's aspects of programming do you enjoy? "
prompt += "\n(Press 'q' to quit)\n"

while True:
    answer = input(prompt)
    if answer == 'q':
        break
    #Added optional random response for each input provided
    else:
        variable = randint(1,3)
        if variable == 1:
            print("Good reason!")
        elif variable == 2:
            print("Great answer!")
        elif variable == 3:
            print("Keep it going!")
        with open(filename, 'a') as file_object:
            file_object.write(answer + "\n")