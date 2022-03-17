import requests
import os
import exsultate.song
import exsultate.generator
import json

BASE_URL = 'http://spiewnik.kamuzo.net/wp-json/exsultate/v1/'

def song(id):
    r = requests.get(BASE_URL + 'song/' + str(id))
    return r.text

def songs(ids_string):
    r = requests.get(BASE_URL + 'songs/' + ids_string)
    return r.text

def songbook(ids_string):
    r = requests.get(BASE_URL + 'songs/' + ids_string)
    dictionary = json.loads(r.text)
    songbook = exsultate.song.SongBook.from_dict(dictionary)
    generator = exsultate.generator.Generator()
    generator.load_configuration()
    output = generator.generate(songbook)
    return output