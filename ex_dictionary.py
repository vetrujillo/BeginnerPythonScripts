#kayna_info = {
#	'first_name': 'Kayna',
#	'last_name': 'Trujillo',
#	'age': 26,
#	'city': 'San Diego',
#}

#for value in kayna_info:
#	print(kayna_info[value])

fav_numbers = {
	'daniel': 17,
	'danny': 9,
	'jeremy': 12,
	'yolie': 8,
	'kayna': 31,
}

#Different from the above method, another way to loop through dictionary. items() function required to specify both key and value
for key, val in fav_numbers.items():
	print(key.capitalize() + "'s favorite number is " + str(val))