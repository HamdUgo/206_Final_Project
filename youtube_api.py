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
    
def data_by_title(title):
    search_url = "https://www.googleapis.com/youtube/v3/search"
    search_params = {
        "part": "snippet",
        "q": title,
        "type": "video",
        "videoCategoryId": "10",
        "key": API_KEY,
        "maxResults": 1
    }

    data = requests.get(search_url, params=search_params)
    if data.status_code == 200:
        search_data = data.json()
        if not search_data.get("items"):
            return {"message": f"No music video found for the title '{title}'"}

        video_id = search_data["items"][0]["id"]["videoId"]

        video_params = {
            "part": "snippet,statistics",
            "id": video_id,
            "key": API_KEY
        }
        video_url = "https://www.googleapis.com/youtube/v3/videos"
        video_data = requests.get(video_url, params=video_params)
        if video_data.status_code == 200:
            video_data = video_data.json()
            if not video_data.get("items"):
                return {"message": f"Details not found for video ID '{video_id}'"}
            
            video_info = video_data["items"][0]
            title_id = video_info["id"]
            title = video_info["snippet"]["title"]
            views = video_info["statistics"].get("viewCount", "0")
            likes = video_info["statistics"].get("likeCount", "0")
            channel = video_info["snippet"]["channelTitle"]

            return {
                "title_id": title_id,
                "title": title,
                "views": views,
                "likes": likes,
                "channel": channel
            }
        else:
            print("error 2")
            return []
    else:
        print("error 1")
        return []
    
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

# function calls to test if functions work
data = data_request('US', 15)
vid_list = most_popular_videos(data)
print(vid_list)
print(len(vid_list))

song_title = "Blinding lights" 
video_details = data_by_title(song_title)
print(video_details)

