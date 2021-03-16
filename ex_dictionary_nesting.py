cities = {
	'el paso': {
		'country': 'the united states',
		'population': 951000,
		'fact': "western-most Texas city",
	},
	"st. andrews": {
		'country': 'scotland',
		'population': 17580,
		'fact': 'oldest university in Scotland',
	},
	'seoul': {
		'country': 'the republic of korea',
		'population': 9700000,
		'fact': 'capital of south korea',
	},
}

for city, dictionary in cities.items():
	print("\nThis is the city of " + city.title())
	print(city.title() + " is located in " + dictionary['country'].title())
	print("It has a population of " + str(dictionary['population']))
	if dictionary['population'] >= 1000000:
		print("That's a lot of people!")
	print("Here's a quick fact about " + city.title() + ":\nIt is the " + dictionary['fact'])