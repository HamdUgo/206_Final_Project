import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# Make sure to type "pip install spotipy --upgrade" in terminal to use spotipy
# here is a guide for spotipy: https://spotipy.readthedocs.io/en/2.24.0/#getting-started

id = "96c0eaa3eb774eb4a1ddbcc8db88e3fc"
secret_id = "907e866598ad4cfcb9038fdcae86f4cd"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= id,
                                               client_secret= secret_id,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read"))

# Searches API by query and returns a list of dictionaries containin track data
def fetch_track_data(query, limit):
    fetch_data = sp.search(q=query, type= 'track', limit= limit)
    track_data = []

    for track in fetch_data['tracks']['items']:
        track_data.append(
            {'track_id':track['id'],
             'title': track['name'],
            'artist': track['artists'][0]['name'],
            'popularity': track['popularity']}
        )
    
    return track_data

#saves data from API to a JSON file
def save_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

#updates JSON file with new data
def update_json(new_data, file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except:
        data = []
    
    data.extend(new_data)

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
