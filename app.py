from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('mainpage.html')


@app.post('/song-info')
def song_info():
    return;


if __name__=='__main__':
    app.run(debug= True)