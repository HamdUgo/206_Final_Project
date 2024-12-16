import requests
import json

API_KEY = 'AIzaSyA51rPuo9cvxTta8y1G0zPf3sjct0-lah8'
BASE_URL = 'https://www.googleapis.com/youtube/v3/videos'

# params: region(string), limit(int)
# limit can only be <= 30
# makes a data request to the Youtube API
def data_request(region, limit):
    params = {
        'part': 'snippet,statistics',
        'chart': 'mostPopular',
        'regionCode': region,
        'videoCategoryId': '10',       
        'maxResults': limit,              
        'key': API_KEY                 
    }
    data = requests.get(BASE_URL, params=params)
    return data

# takes the data from the API and returns a list of the most popular music videos on youtube
def most_popular_videos(data):
    if data.status_code == 200:
        data = data.json()
        videos = []
        for vid in data.get('items', []):
            video_id = vid['id']
            title = vid['snippet']['title']
            views = vid['statistics'].get('viewCount', 'N/A')
            likes = vid['statistics'].get('likeCount', 'N/A')
            # print(f"video ID: {video_id}")
            # print(f"title: {title}")
            # print(f"views: {views}")
            # print(f"likes: {likes}")
            # print("\n")
            videos.append(
                {
                    "video_id": video_id,
                    "title": title,
                    "views": views,
                    "likes": likes
                }
            )
        return videos
    else:
        print("Error")
        return []

def save_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

# function calls to test if functions work
data = data_request('US', 15)
vid_list = most_popular_videos(data)
print(vid_list)
print(len(vid_list))

