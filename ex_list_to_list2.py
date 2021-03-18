sandwich_order = ['tuna', 'pastrami', 'ham', 'pastrami', 'steak', 'cheese', 'pastrami']
finished_sandwiches = []

#Checks if specified string is in list
if 'pastrami' in sandwich_order:
	#If so, it will run the following code
	print("Sorry, we are out of that ingredient")

#While the specified string is in the list, the ensuing code will run
while 'pastrami' in sandwich_order:
	#Removes specfied string from list
	sandwich_order.remove('pastrami')

#Loop will run until specified list is empty
while sandwich_order:
	#Pulls last item from list and stores it in 'sandwich'
	sandwich = sandwich_order.pop()
	print("\nYour " + sandwich + " sandwich is ready.")
	#Adds value of sandwich into list finished_sandwiches
	finished_sandwiches.append(sandwich)

print(finished_sandwiches)	