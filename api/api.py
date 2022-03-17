import flask
from requests.sessions import InvalidSchema
import kamuzo
import os

application = flask.Flask(__name__)

@application.route('/', methods=['GET'])
def home():
    return "<p>This is not a website server. It only provides microservices.</p>"

@application.route('/api/v1/songbook/<ids_string>', methods=['GET'])
def generate_songbook(ids_string):
    filename = kamuzo.songbook(ids_string)
    directory = os.path.dirname(os.path.realpath(__file__)) + "/exsultate"
    try:
        return flask.send_from_directory(directory, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

@application.route('/api/v1/song/<int:id>', methods=['GET'])
def obtain_song(id):
    return kamuzo.song(id)

@application.route('/api/v1/songs/<ids_string>', methods=['GET'])
def obtain_songs(ids_string):
    return kamuzo.songs(ids_string)

if __name__ == "__main__":
    application.debug = False
    application.run(port=8080)