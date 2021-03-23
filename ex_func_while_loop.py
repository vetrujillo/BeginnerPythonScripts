def make_album(artist_name, album_name, track_number=''):
	"""Builds dictionary with album info"""
	unified = {
		'artist': artist_name.title(),
		'album': album_name.title(),
	}
	if track_number:
		unified['tracks'] = track_number

	return unified

while True:
	print("\nEnter an artist or band here:")
	print("(Enter 'q' anytime to quit)")

	a_name = input("Artist/band: ")
	if a_name == 'q':
		break

	al_name = input("Album: ")
	if al_name == 'q':
		break

	formatted = make_album(a_name, al_name)
	for k, v in formatted.items():

		print("\n" + k.title() + ": " + v.title()) 