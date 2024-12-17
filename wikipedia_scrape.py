from bs4 import BeautifulSoup 
import requests
import json

def get_wiki_songs(link): 
    response = requests.get(link)
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('tbody')
        rows = table.find_all('td')

        a_list = []
        for row in rows:
            if row.find('a'):
                a_list.append(row)

        song_list = []
        for a in a_list:
            if '"' in a:
                song_list.append(a.text.strip('"'))
            if '"' not in a:
                continue

        song_list[19] = song_list[19].strip('"\n')

        return song_list

    else:
        print("Invalid URL")
        return

def get_wiki_artists(link): 
    response = requests.get(link)
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('tbody')
        rows = table.find_all('td')

        a_list = []
        for row in rows:
            if row.find('a'):
                a_list.append(row)
        
        artist_list = []
        for a in a_list:
            if '"' in a:
                continue
            if '"' not in a:
                artist_list.append(a.text.strip())
        
        artist_list.insert(18, 'SZA')

        return artist_list
    
    else:
        print("Invalid URL")
        return
    
def create_file_data(songs, artists):
    top_100 = []
    for i in range(100):
        temp = {}
        song = songs[i]
        artist = artists[i]
        temp['Song Title'] = song
        temp['Artist(s)'] = artist
        temp['Ranking'] = i + 1
        top_100.append(temp)
    
    return top_100  

def create_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent = 3)


song_100 = get_wiki_songs('https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2024#Year-end_list')
artist_100 = get_wiki_artists('https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2024#Year-end_list')
billboard_100 = create_file_data(song_100, artist_100)
create_json(billboard_100, 'billboard.json')
