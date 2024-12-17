import matplotlib.pyplot as plt
import numpy as np

def scatter_plot():
    # Place holders
    spotify_popularity = []
    lastfm_playcount = []

    plt.figure(figsize=(8, 6))
    plt.scatter(spotify_popularity, lastfm_playcount, c='blue', edgecolors='black')
    plt.xlabel('Spotify Popularity')
    plt.ylabel('Last.fm Playcount')
    plt.title('Correlation Between Spotify Popularity and Last.fm Playcount')
    plt.tight_layout()
    plt.show()

def bar_chart():
    # Place holder
    tracks = []
    spotify_popularity = []
    lastfm_playcount = []

    x = np.arange(len(tracks))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, spotify_popularity, width, label='Spotify Popularity')
    plt.bar(x + width/2, lastfm_playcount, width, label='Last.fm Playcount')

    plt.xticks(x, tracks, rotation=45)
    plt.ylabel('Metrics')
    plt.title('Comparison of Spotify Popularity and Last.fm Playcount')
    plt.legend()
    plt.tight_layout()
    plt.show()

def box_plot():
    # Place holder
    spotify_popularity = []
    lastfm_playcount = []

    data = [spotify_popularity, lastfm_playcount]

    plt.figure(figsize=(8, 6))
    plt.boxplot(data, labels=['Spotify Popularity', 'Last.fm Playcount'])
    plt.title('Distribution of Popularity and Playcounts')
    plt.ylabel('Values')
    plt.tight_layout()
    plt.show()


