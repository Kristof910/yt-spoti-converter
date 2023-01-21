from api import *
import setup

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/endpoint", methods=["POST"])
def endpoint():
    try:
        data = request.get_json()
        yt_playlist = data["yt_playlist"]
        spoti_token = data["spoti_token"]
        spoti_user_id = data["spoti_user_id"]
        
        yt_songs = get_yt_songs(setup.yt_api_key, yt_playlist)
        playlist_id = create_spoti_playlist(spoti_token, spoti_user_id, "YT Converted")
        add_spoti_songs(spoti_token, yt_songs, playlist_id)
        
        return jsonify({"message" : "data succesfully received"})

    except Exception as e:
        return jsonify({"message" : "an error has occured"})

if __name__ == '__main__':
    app.run(port=1234)
