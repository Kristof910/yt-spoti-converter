from api import *
import setup

def main():
    yt_songs = get_yt_songs(setup.yt_api_key, setup.yt_playlist)
    playlist_id = create_spoti_playlist(setup.spoti_token, setup.spoti_user_id, "YT Converted")
    add_spoti_songs(setup.spoti_token, yt_songs, playlist_id)
    

if __name__ == '__main__':
    main()
