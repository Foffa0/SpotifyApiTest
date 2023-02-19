from flask import Blueprint
# Import image class of matplotlib
from colorthief import ColorThief
from PIL import Image
import requests
from io import BytesIO

song = Blueprint('song', __name__)

class Song():

    def __init__(self, data):
        self.data = data
        self.title = self.data["item"]["name"]
        self.image = self.data["item"]["album"]["images"][0]["url"]
        self.artists = []
        for id, artist in enumerate(self.data["item"]["artists"]):
            self.artists.append(artist["name"])
        self.album = self.data["item"]["album"]["name"]
        
        response = requests.get(self.image)
        color_thief = ColorThief(BytesIO(response.content))
        # get the dominant color
        self.scheme_color = color_thief.get_color(quality=1)