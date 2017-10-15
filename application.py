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
def showArtists():
	artists = session.query(Artist).all()
	return render_template('catalog.html', artists = artists)

# Show the tracks available for an artist
@app.route('/catalog/<string:artist_name>/tracks')
def showTracks(artist_name):
	artist = session.query(Artist).filter_by(name = artist_name).one()
	tracks = session.query(Track).filter_by(artist_id = artist.id).all()
	return render_template('tracks.html', tracks = tracks, artist = artist)

# Show the information of a track
@app.route('/catalog/<string:artist_name>/<string:track_title>')
def showTrack(artist_name, track_title):
	artist = session.query(Artist).filter_by(name = artist_name).one()
	track = session.query(Track).filter_by(artist_id = artist.id, title = track_title).one()
	return render_template('track.html', track = track, artist = artist)

# Edit track
@app.route('/catalog/<int:artist_id>/<int:track_id>/edit')
def editTrack(artist_id, track_id):
	artist = session.query(Artist).filter_by(id = artist_id).one()
	track = session.query(Track).filter_by(id = track_id).one()
	return render_template('edittrack.html', track = track, artist = artist)

# Delete track
@app.route('/catalog/<int:artist_id>/<int:track_id>/delete')
def deleteTrack(artist_id, track_id):
	artist = session.query(Artist).filter_by(id = artist_id).one()
	track = session.query(Track).filter_by(id = track_id).one()
	return render_template('deletetrack.html', track = track, artist = artist)

# Add track
@app.route('/catalog/add')
def addTrack():
	return render_template('addtrack.html')

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