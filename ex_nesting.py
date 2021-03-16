apollo = {
	'name': 'apollo',
	'species': 'cat',
	'owner': 'kayna',
}

artemis = {
	'name': 'artemis',
	'species': 'cat',
	'owner': 'kayna',
}

ursa = {
	'name': 'ursa',
	'species': 'dog',
	'owner': 'victor',
}

pets = [apollo, artemis, ursa]

for pet in pets:
	print("This is " + pet['name'].title() + "! " + pet['name'].title() + " is a " + 
	pet['species'] + ". " + pet['name'].title() + "'s owner is " + pet['owner'].title())