import flask
from requests.sessions import InvalidSchema
import kamuzo
import os
from io import BytesIO

application = flask.Flask(__name__)

@application.route('/', methods=['GET'])
def home():
    return "<p>This is not a website server. It only provides microservices.</p>"

@application.route('/api/v1/songbook/<ids_string>', methods=['GET'])
def generate_songbook(ids_string):
    mem = kamuzo.songbook(ids_string)
    mem.seek(0)
    try:
        #return flask.send_from_directory(directory, filename, as_attachment=True)
        return flask.send_file(
            mem,
            as_attachment=True,
            attachment_filename='ulotka.docx',
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
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