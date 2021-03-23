#Creates function with 3 parameters, the 3rd accepting multiple keyword
#arguments
def make_car(manu, mod, **car_info):
	"""Stores car info"""
	#Create the dictionary to store info
	car = {}
	#Set key-value pairs equal to arguments provided
	car['manufacturer'] = manu
	car['model'] = mod

	#Since **car_info creates a dictionary item, key values need to be pulled
	for key, value in car_info.items():
		car[key] = value

	return car

chosen_car = make_car('toyota', 'corolla', color='grey',
	year=2013)

print(chosen_car)