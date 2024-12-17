from tikapi import TikAPI, ValidationException, ResponseException
import json

API_KEY = 'BzUf0VvqpyhrPNjcREqVAOyp1sPsArvrqWyKSVxffYDPP7sW'
api = TikAPI(API_KEY)

def fetch_music_ids_from_trending_videos(limit):
    """
    Extract music IDs from trending videos.
    :param limit: The number of music IDs to fetch.
    :return: List of music IDs with metadata.
    """
    try:
        response = api.public.explore(
            session_id="d7091fb7b7399e027cc08833c0597654",  # This session doesn't work, am gonna try to fix it
            country="us"
        )
        trending_videos = response.body.get("aweme_list", [])

        music_ids = []
        for video in trending_videos:
            music = video.get("music", {})
            music_id = music.get("id")
            if music_id and len(music_ids) < limit:
                music_ids.append({
                    "music_id": music_id,
                    "title": music.get("title"),
                    "author_name": music.get("author"),
                })

            if len(music_ids) >= limit:
                break

        return music_ids

    except ValidationException as e:
        print(f"Validation error: {e}, Field: {e.field}")
        return []
    except ResponseException as e:
        print(f"Response error: {e}, Status Code: {e.response.status_code}")
        return []

top_music_ids = fetch_music_ids_from_trending_videos(limit=10)

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

print(f"Fetched {len(top_music_ids)} music IDs from trending videos.")
for music in top_music_ids[:5]:
    print(music)



