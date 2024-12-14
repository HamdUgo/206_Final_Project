import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="96c0eaa3eb774eb4a1ddbcc8db88e3fc",
                                               client_secret="907e866598ad4cfcb9038fdcae86f4cd",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read"))



