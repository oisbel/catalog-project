from flask import Flask, render_template, request, redirect,jsonify, url_for, flash

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database import Base, User, Artist, Track

app = Flask(__name__)

#Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show the artists and latest tracks
@app.route('/')
def showArtist():
	return "main page"

# Show the tracks available for an artist
@app.route('/catalog/<string:artist_name>/tracks')
def showItems(artist_name):
	return "Items in {}".format(artist_name)

# Show the information of a track
@app.route('/catalog/<string:artist_name>/<string:track_title>')
def showItem(artist_name, track_title):
	return "{} in {}".format(track_title,artist_name)

# Add track
@app.route('/catalog/add')
def addItem():
	return "Add Item"

# Edit track
@app.route('/catalog/<string:artist_name>/<string:track_title>/edit')
def showCategory(artist_id, track_title):
	return "Edit {}".format(track_title)

# Delete track
@app.route('/catalog/<string:artist_name>/<string:track_title>/delete')
def deleteCategory(artist_id, track_title):
	return "Delete {}".format(track_title)

# JSON API to view the catalog
@app.route('/catalog.json')
def artistsJSON():
	artists = session.query(Artist).all()
	artists_tup=[]
	for artist in artists:
		tracks = session.query(Track).filter_by(artist_id = artist.id).all()
		tracks_tup = artist.serialize
		tracks_tupA = []
		for track in tracks:
			tracks_tupA.append(track.serialize)
		tracks_tup['Tracks']=tracks_tupA
		artists_tup.append(tracks_tup)
	return jsonify(Artists = artists_tup)

if __name__ == '__main__':
  app.secret_key = '88040422507vryyo'
  app.debug = True
  app.run(host = '0.0.0.0', port = 8000)