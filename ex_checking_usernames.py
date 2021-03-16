current_users = ['fox', "admin", "bobo", "V", "guest"]
new_users = ['fox', 'sun', 'Guest', 'apollo', 'artemis']

for user in new_users:
	if user.lower() in current_users:
		print("Sorry, that username is taken.")
	else:
		print("That username is available")
