from flask import Flask, render_template, request
from config import Config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)
app.config.from_object(Config)

client_credentials = SpotifyClientCredentials(Config.SPOTIFY_CLIENT_ID,Config.SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager =client_credentials)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('mainpage.html')


@app.post('/song-info')
def song_info():
    song_name = request.form.get('song_name')
    song = sp.search(q=song_name,limit = 1)
    print(song)
    return "OK", 200


if __name__=='__main__':
    app.run(debug= True)