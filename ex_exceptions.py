print("Please enter two numbers. \nType 'q' to quit")

while True:
    first = input("Enter the first number here: ")
    if first == 'q':
        break

    second_number = input("Enter the second number here: ")
    if second_number == 'q':
        break
    
    try:
        print(int(first) + int(second_number))
    except ValueError:
        print("Please enter a valid integer")
    