def make_shirt(size='large', text='I Love Python'):
	"""Function using default arguments"""
	print("\nYou have chosen shirt size: " + size)
	print("The text you have chosen is: " + text)

make_shirt()

make_shirt('medium')

make_shirt(size='small', text='Hello')