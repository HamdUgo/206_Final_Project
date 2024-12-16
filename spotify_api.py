import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# Make sure to type "pip install spotipy --upgrade" in terminal to use spotipy
# here is a guide for spotipy: https://spotipy.readthedocs.io/en/2.24.0/#getting-started
# Popularity is calculated from 0-100(100 being the most popular)
# Popularity is based on CURRENT streams not past streams
# This is specified in more detail here -> eveloper.spotify.com/documentation/web-api/reference/get-an-artists-top-tracks

id = "96c0eaa3eb774eb4a1ddbcc8db88e3fc"
secret_id = "907e866598ad4cfcb9038fdcae86f4cd"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= id,
                                               client_secret= secret_id,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="playlist-read-private playlist-read-collaborative"))

# Searches API by query and returns a list of dictionaries containing track data
def track_data(query, limit):
    fetch_data = sp.search(q=query, type= 'track', limit= limit)
    track_data = []

    for track in fetch_data['tracks']['items']:
        track_data.append(
            {
            'track_id':track['id'],
            'title': track['name'],
            'artist': track['artists'][0]['name'],
            'popularity': track['popularity']
            }
        )
    
    return track_data

# Finds the Top 10 tracks of an artist
def artist_top_tracks(artist_name):
    fetch_data = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    artist_id = fetch_data['artists']['items'][0]['id']
    top_tracks = sp.artist_top_tracks(artist_id)
    track_data = []

    for track in top_tracks['tracks']:
        track_data.append(
            {
            'track_id': track['id'],
            'title': track['name'],
            'artist': track['artists'][0]['name'],
            'popularity': track['popularity']
            }
        )

    return track_data

# returns track information from all tracks in a playlist
# Will use this to check top 50 playlist or Top hit playlist
def playlist_data(playlist_id):
    playlist = sp.playlist_tracks(playlist_id)
    track_data = []

    for item in playlist['items']:
        track = item['track']
        track_data.append(
            {
            'track_id':track['id'],
            'title': track['name'],
            'artist': track['artists'][0]['name'],
            'popularity': track['popularity']
            }
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

# Testing to get Billboard Top 100 using playlist_data
playlist_id = "https://open.spotify.com/playlist/6UeSakyzhiEt4NB3UAd6NQ"
p_data = playlist_data(playlist_id)
print("\nPlaylist Data:")
for track in p_data:
    print(track)

# Testing artists_top_tracks
top_tracks = artist_top_tracks("King Von")
print("\nVon's Top Track's")
for track in top_tracks:
    print(track)

# Testing track_data
t_data = track_data("Kanye West", limit=50)
print("\n Track Data")
for track in t_data:
    print(track)
