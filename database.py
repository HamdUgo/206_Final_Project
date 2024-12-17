import sqlite3
import os

def set_up_database():
    path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(path, 'database.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXIST tiktok(
        video_id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        likes INTEGER,
        views INTEGER
        );
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXIST youtube(
        video_id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        views INTEGER,
        likes INTEGER
        );
        """
    )
    cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS spotify(
        track_id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        artist TEXT,
        popularity INTEGER
    );
    '''
    )
