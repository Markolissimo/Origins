from flask import Flask, render_template, request, jsonify
from config import Config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)
app.config.from_object(Config)

client_credentials = SpotifyClientCredentials(Config.SPOTIFY_CLIENT_ID, Config.SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('mainpage.html')

@app.route('/song-info', methods=['POST'])
def song_info():
    song_name = request.form.get('song_name')
    result = sp.search(q=song_name, limit=10)

    if result and 'tracks' in result and 'items' in result['tracks']:
        original_tracks = []
        similar_songs = []

        for track in result['tracks']['items']:
            track_info = {
                'song_name': track['name'],
                'artist': track['artists'][0]['name'],
                'release_date': track['album']['release_date'],
                'url': track['external_urls']['spotify'],
                'cover_image': track['album']['images'][0]['url']
            }

            if track_info not in original_tracks:
                original_tracks.append(track_info)
            else:
                similar_songs.append(track_info)

        if original_tracks:
            return render_template('song.html', original_track=original_tracks[0], similar_songs=similar_songs)

    return jsonify({'error': 'Song not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
