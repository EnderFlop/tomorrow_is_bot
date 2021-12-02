import requests
import tweepy
import os
from TwitterAPI import TwitterAPI
from dotenv import load_dotenv
from image_creator import create_image

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

try:
  api.verify_credentials()
  print("Authentication OK")
except:
  print("Error during authentication")

create_image()

api.update_status_with_media("", "image.png")