import sqlite3
import os
import json

def read_spotify_data():
    full_path = os.path.join(os.path.dirname(__file__), 'spotify.json')
    f = open(full_path)
    file_data = f.read()
    f.close()
    spotifyjson_data = json.loads(file_data)
    return spotifyjson_data

def read_billboard_data():
    full_path = os.path.join(os.path.dirname(__file__), 'billboard.json')
    f = open(full_path)
    file_data = f.read()
    f.close()
    billboardjson_data = json.loads(file_data)
    return billboardjson_data

def read_lastfm_data():
    full_path = os.path.join(os.path.dirname(__file__), 'lastfm.json')
    f = open(full_path)
    file_data = f.read()
    f.close()
    lastfmjson_data = json.loads(file_data)
    return lastfmjson_data

def set_up_database():
    path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(path, 'database.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    return conn, cur

def set_up_spotify_table(data, conn, cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS spotify(
        track_id TEXT NOT NULL,
        title TEXT NOT NULL,
        artist TEXT NOT NULL,
        popularity INTEGER NOT NULL)
        """
    )

    count = 0
    i = 0
    while count < 25 and  i < len(data):
        cur.execute("SELECT track_id FROM spotify WHERE track_id = ?", (data[i]['track_id'],))
        if not cur.fetchone():
            cur.execute(
                """
                INSERT OR IGNORE INTO spotify(track_id, title, artist, popularity)
                VALUES (?, ?, ?, ?) 
                """, (data[i]['track_id'], data[i]['title'], data[i]['artist'], data[i]['popularity'])
            )
            count += 1
            i += 1
        else:
            i +=1

    conn.commit()

def set_up_billboard_table(data, conn, cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS billboard(
        songtitle TEXT NOT NULL,
        artist TEXT NOT NULL,
        ranking INTEGER NOT NULL)
        """
    )

    count = 0
    i = 0
    while count < 25 and  i < len(data):
        cur.execute("SELECT ranking FROM billboard WHERE ranking = ?", (data[i]['Ranking'],))
        if not cur.fetchone():
            cur.execute(
                """
                INSERT OR IGNORE INTO billboard(songtitle, artist, ranking)
                VALUES (?, ?, ?) 
                """, (data[i]['Song Title'], data[i]['Artist(s)'], data[i]['Ranking'])
            )
            count += 1
            i += 1
        else:
            i +=1

    conn.commit()

def set_up_lastfm_table(data, conn, cur):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS lastfm(
        artist TEXT NOT NULL,
        track TEXT NOT NULL,
        playcount INTEGER NOT NULL,
        listeners INTEGER NOT NULL
        )
        """
    )

    count = 0
    i = 0
    while count < 25 and  i < len(data):
        cur.execute("SELECT track FROM lastfm WHERE track = ?", (data[i]['track'],))
        if not cur.fetchone():
            cur.execute(
                """
                INSERT OR IGNORE INTO lastfm(artist, track, playcount, listeners)
                VALUES (?, ?, ?, ?) 
                """, (data[i]['artist'], data[i]['track'], data[i]['playcount'], data[i]['listeners'])
            )
            count += 1
            i += 1
        else:
            i +=1

    conn.commit()

spotify_data = read_spotify_data()
billboard_data = read_billboard_data()
lastfm_data = read_lastfm_data()

conn, cur = set_up_database()

set_up_spotify_table(spotify_data, conn, cur)
set_up_billboard_table(billboard_data, conn, cur)
set_up_lastfm_table(lastfm_data, conn, cur)