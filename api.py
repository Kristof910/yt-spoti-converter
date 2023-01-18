import requests
import json

def get_yt_songs(api_key, playlist_link):
    try:
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_link}&key={api_key}"

        while True:
            response = requests.get(url)
            data = json.loads(response.text)

            list = []
            for item in data["items"]:
                list.append(item["snippet"]["title"])

            if "nextPageToken" in data:
                url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_link}&key={api_key}&maxResults=50&pageToken={data['nextPageToken']}"
            else:
                break    

        return list 
           
    except Exception as e:
        print(f"Ops, something gone wrong: {e}")

def create_spoti_playlist(api_key):
    pass

def add_spoti_songs(api_key, list):
    pass