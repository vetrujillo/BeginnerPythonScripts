fav_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

take_poll = ['jen', 'chris', 'phil', 'mary', 'kayna', 'victor']

for name in take_poll:
	if name in fav_languages.keys():
		print(name.title() + ", thank you for responding!")
	else:
		print(name.title() + ", please take the poll")