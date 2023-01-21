import requests
import json

def get_yt_songs(api_key, playlist_link):
    try:
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_link}&key={api_key}"

        list = []
        while True:
            response = requests.get(url)
            data = json.loads(response.text)

            for item in data["items"]:
                list.append(item["snippet"]["title"])

            if "nextPageToken" in data:
                url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_link}&key={api_key}&maxResults=50&pageToken={data['nextPageToken']}"
            else:
                break    

        return list 
           
    except Exception as e:
        print(f"Ops, something gone wrong in get_yt_songs: {e}")

def create_spoti_playlist(token, user_id, playlist_name):
    try:
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        playlist_data = {
            "name": playlist_name,
            "description": "test"
        }

        response = requests.post(f"https://api.spotify.com/v1/users/{user_id}/playlists", headers=headers, data=json.dumps(playlist_data))
        return response.json()['id']

    except Exception as e:
        print(f"Ops, something gone wrong in create_spoti_playlist: {e}")

def add_spoti_songs(token, list, playlist_id):
    try:
        for song in list:
            headers = {'Authorization': 'Bearer ' + token}
            search_url = 'https://api.spotify.com/v1/search?q={}&type=track&limit=1'.format(song)
            response = requests.get(search_url, headers=headers)
            song_id = response.json()['tracks']['items'][0]['id']

            headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
            add_url = 'https://api.spotify.com/v1/playlists/{}/tracks?uris=spotify:track:{}'.format(playlist_id,song_id)
            response = requests.post(add_url, headers=headers)

    except Exception as e:
        print(f"Ops, something gone wrong in add_spoti_songs: {e}")