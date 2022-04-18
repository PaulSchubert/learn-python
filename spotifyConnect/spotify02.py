import spotipy
import json
import webbrowser

username = 'Your_Username'
clientID = 'Your_Client_ID'
clientSecret = 'Your_Client_Secret'
redirectURI = 'http://google.com/'

#create OAuth Object
oath_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirectURI)

#Create token
token_dict = oath_object.get_access_token()
token = token_dict['access_token']

#Create Spotify Object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

#printing the response better to read:
print(json.dumps(user, sort_keys = True, indent = 4))


while True:
	print ('Welcome, ' + user['display_name'])
	print ('0 - Exit')
	print ('1 - Search for a song')
	choice = int(input('Your Choice: '))

	if choice == 1:
		#Get the song name
		searchQuery = raw_input('Enter Song Name: ')
	
		#Search for the song
		searchResults = spotifyObject.search(searchQuery,1,0,'track')

		#Get required sata from JSON response
		tracks_dict = searchResults['tracks']
		tracks_items = tracks_dict['items']
		song = tracks_items[0]['external_urls']['spotify']

		#Open the song in Web Browser
		webbrowser.open(song)

		print('Song has opened in your browser')

	elif choice == 0:
		break
	
	else:
		print('Enter valid choice. ')


