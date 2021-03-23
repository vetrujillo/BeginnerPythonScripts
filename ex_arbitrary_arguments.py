def make_sandwich(*fillings):
	"""Summary of sandwich order"""
	print("\nMaking sandwich with following ingredients:")
	for filling in fillings:
		print(filling)

make_sandwich('ham')
make_sandwich('ham', 'cheese', 'tomato')
make_sandwich('bacon', 'lettuce')