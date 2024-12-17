import requests
import json

API_KEY = '8a8d8e3774f7e581551e1fc927dbedd5'
SHARED_SECRET = 'fa3180fba69fdc676c5f0410638c29ec'

BASE_URL = "http://ws.audioscrobbler.com/2.0/"

def top_tracks(limit):
    params = {
        "method": "chart.gettoptracks",
        "api_key": API_KEY,
        "format": "json",
        "limit": limit
    }
    fetch_data = requests.get(BASE_URL, params=params)
    if fetch_data.status_code == 200:
        data = fetch_data.json()
        tracks = data['tracks']['track']
        track_list = []
        for track in tracks:
            track_info = {
                "artist": track['artist']['name'],
                "track": track['name'],
                "playcount": int(track['playcount']),
                "listeners": int(track['listeners'])
            }
            track_list.append(track_info)
        
        return track_list
    else:
        print("Error fetching data:", fetch_data.status_code)
        return []
    
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
    

print("Fetching data from Last.fm API...")
tracks = top_tracks(100)
if tracks:
    print(tracks)
else:
    print('error')