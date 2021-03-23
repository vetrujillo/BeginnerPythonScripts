#Initial list to start with
magicians = ['houdini', 'copperfield', 'blaine']

def show_magicians(magician_list):
	"""Pulls values from list and prints"""
	for magician in magician_list:
		print(magician.title())

def make_great(magicians):
	"""Add Great to each magician's name"""
	great_magicians = []
	#Starts loop through initial list
	while magicians:
		#Removes the last value from magician list, adds 'the Great', stores in new variable
		the_great = magicians.pop() + " the Great"
		#Adds previous variable into great_magicians list
		great_magicians.append(the_great.title())

	#Pulls each value from the newly created list	
	for great_magician in great_magicians:
		#Adds modified values back into original list
		magicians.append(great_magician)	

#Prints the original list, unmodified
show_magicians(magicians)

make_great(magicians[:])