import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Make sure to type "pip install spotipy --upgrade" in terminal to use spotipy
# here is a guide for spotipy: https://spotipy.readthedocs.io/en/2.24.0/#getting-started

id = "96c0eaa3eb774eb4a1ddbcc8db88e3fc"
secret_id = "907e866598ad4cfcb9038fdcae86f4cd"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= id,
                                               client_secret= secret_id,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read"))