import os
import sys
from flask import Flask, request, render_template
from lib.album_repository import AlbumRepository
from lib.albums import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("/albums/index.html", albums=albums)

@app.route('/1', methods=['GET'])
def get_album_1():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/1.html", albums=albums)

@app.route('/2', methods=['GET'])
def get_album_2():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/2.html", albums=albums)

@app.route('/albums/<id>')
def find_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template('albums/show.html', album=album)

@app.route('/artists', methods=['GET'])
def get_artists_list():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template("/artists/index.html", artists=artists)

@app.route('/artists/<id>')
def find_an_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template('artists/show.html', artist=artist)

@app.route('/albums', methods=['POST'])
def add_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None, 
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id'])
    repository.create(album)
    return '', 200

# @app.route('/artists')    
# def get_artists():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artists = repository.all()
#     artist_string = [f"{artist}" for artist in artists]
#     return "\n".join(artist_string)

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        None,
        request.form['name'],
        request.form['genre']
    )
    repository.create(artist)
    return "", 200

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
