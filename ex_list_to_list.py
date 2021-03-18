sandwich_order = ['tuna', 'ham', 'steak', 'cheese']
finished_sandwiches = []

while sandwich_order:
	sandwich = sandwich_order.pop()
	print("Your " + sandwich + " sandwich is ready.")

	finished_sandwiches.append(sandwich)
