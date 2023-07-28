from os import environ as env
from dotenv import load_dotenv

load_dotenv('.env.dev')
class Config:
    SPOTIFY_CLIENT_ID = env.get('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = env.get('SPOTIFY_CLIENT_SECRET')
    APP_SECRET_KEY = env.get('APP_SECRET_KEY')