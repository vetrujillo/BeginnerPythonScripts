def build_profile(first, last, **user_info):
	"""Buiild dict containing info about user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last

	for key, value in user_info.items():
		profile[key] = value

	return profile

user_profile = build_profile('victor', 'trujillo', location='san diego',
	field='cybersecurity')

print(user_profile)