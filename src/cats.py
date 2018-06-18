import requests
import os

"""
    http://thecatapi.com/
"""

CAT_API_KEY = os.environ.get('CAT_API_KEY')

class Cat():
    def getCat(self):
        response = requests.get(
            "http://thecatapi.com/api/images/get?api_key={}&format=html".format(CAT_API_KEY))
        imageURL = response.text[response.text.find("src=\"")+5:-7] # Tidy this up!
        return imageURL
