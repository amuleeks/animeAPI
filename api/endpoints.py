from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import csv
import collections

app = Flask(__name__)
api = Api(app)

# character -> [anime, personality, rank]
def read():
    with open('./anime_characters.csv') as csvfile:
        character_map = dict()
        anime_reader = csv.reader(csvfile)
        for line in anime_reader:
            character = line[0]
            anime = line[1]
            personality = line[2]
            rank = line[3]
            character_map[character] = [anime, personality, rank]
        return character_map


class Characters(Resource):
    def get(self):
        character_map = read()
        return character_map, 200
        

api.add_resource(Characters, '/characters')

if __name__ == '__main__':
    app.run()