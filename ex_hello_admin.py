usernames = ['fox', "admin", "bobo", "V", "guest"]

if usernames:
	for user in usernames:
		if user == "admin":
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello " + user + ", thank you for logging in")	
else:
	print("We need to find some users!")
