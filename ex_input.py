#requested_car = input("Hello, what make/model car would you like today? ")
#print(requested_car + "? That is a good choice! I'll check if it is available")


#group_number = input("Good evening, how many people are in your party today? ")
#group_number = int(group_number)

#if group_number > 8:
#	print("There will be a short wait for a party of this size")
#else:
#	print("Your table is ready")

number = input("Please enter a number and I'll report if it is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
	print("This number is a multiple of ten")
else:
	print("This number is not a multiple of ten")