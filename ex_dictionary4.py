fav_places = {
	'victor': ['seoul', 'edinburgh', 'california'],
	'kayna': ['paris', 'rome', 'greece'],
	'tuna': ['the park'],
}

for key, value in fav_places.items():
	if len(value) == 1:
		print("\n" + key.title() + "'s favorite place is: \n" + value[0])
	elif len(value) > 1:
		print("\n" + key.title() + "'s favorite places are: ")
		for location in value:
			print(location.title())
