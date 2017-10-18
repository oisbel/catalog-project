from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify

# For database
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database import Base, User, Artist, Track

# For anti-forgery
from flask import session as login_session
import random
import string

# Imports for Google Connect Function (gconnect)
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login')
def showLogin():
	# Anti-forgery state token and store in the sesion for later validation
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate anti-forgery state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data
    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Check that the access token inside of it is valid sending it to google
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Similary verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response
    # Check to see if user is already logged in
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    # If all the verifications are good mean the user can successfully log in
    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id
    # Get user info from google
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'
    # see if user exists in the database, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("Welcome %s" % login_session['username'])
    print "Successfully login!"
    return output


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        del login_session['gplus_id']
        del login_session['access_token']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash("Successfully disconnected")
        return redirect('/')
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# User Helper Functions
def createUser(login_session):
    newUser = User(
        name=login_session['username'], email=login_session['email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# Show the artists and latest tracks
@app.route('/')
def showArtists():
    artists = session.query(Artist).all()
    count = session.query(Artist).count()
    # latest track added
    tracks = session.query(Track).order_by(desc(Track.id)).limit(count).all()
    # list of list of track,artist
    latest = []
    for track in tracks:
        latest.append([session.query(Artist).filter_by(
            id=track.artist_id).one().name, track.title])
    return render_template(
        'catalog.html', artists=artists, latest=latest)


# Show the tracks available for an artist
@app.route('/catalog/<string:artist_name>/tracks')
def showTracks(artist_name):
    artist = session.query(Artist).filter_by(name=artist_name).one()
    tracks = session.query(Track).filter_by(artist_id=artist.id).all()
    if 'username' not in login_session:
        return render_template(
            'publictracks.html', tracks=tracks, artist=artist)
    else:
        return render_template(
            'tracks.html', tracks=tracks, artist=artist)


# Show the information of a track
@app.route('/catalog/<string:artist_name>/<string:track_title>')
def showTrack(artist_name, track_title):
    artist = session.query(Artist).filter_by(name=artist_name).one()
    track = session.query(Track).filter_by(
        artist_id=artist.id, title=track_title).one()
    creator = getUserInfo(track.user_id)
    if ('username' not in login_session or
            creator.id != login_session['user_id']):
        return render_template(
            'publictrack.html', track=track, artist=artist)
    else:
        return render_template(
            'track.html', track=track, artist=artist)


# Edit track
@app.route('/catalog/<int:artist_id>/<int:track_id>/edit', methods=['GET', 'POST'])
def editTrack(artist_id, track_id):
    if 'username' not in login_session:
        return redirect('/login')
    artist = session.query(Artist).filter_by(id=artist_id).one()
    track = session.query(Track).filter_by(id=track_id).one()
    # in case the user try to access via url
    if track.user_id != login_session['user_id']:
        return "<script>function myFunction(){alert('You are not authorized to edit this track.');}</script><body onload = 'myFunction()'>"
    if request.method == 'POST':
        if request.form['title']:
            track.title = request.form['title']
        if request.form['lyrics']:
            track.lyrics = request.form['lyrics']
        if request.form['video']:
            track.video = request.form['video']
        session.add(track)
        session.commit()
        flash("Track Successfully Edited")
        return redirect(url_for(
            'showTrack', artist_name=artist.name, track_title=track.title))
    else:
        return render_template(
            'edittrack.html', track=track, artist=artist)


# Delete track
@app.route('/catalog/<int:artist_id>/<int:track_id>/delete', methods=['GET', 'POST'])
def deleteTrack(artist_id, track_id):
    if 'username' not in login_session:
        return redirect('/login')
    artist = session.query(Artist).filter_by(id=artist_id).one()
    track = session.query(Track).filter_by(id=track_id).one()
    if track.user_id != login_session['user_id']:
        return "<script>function myFunction(){alert('You are not authorized to delete this track.');}</script><body onload = 'myFunction()'>"
    if request.method == 'POST':
        session.delete(track)
        session.commit()
        flash("Track Successfully Deleted")
        return redirect(url_for('showTracks', artist_name=artist.name))
    else:
        return render_template(
            'deletetrack.html', track=track, artist=artist)


# Add track
@app.route('/catalog/<int:artist_id>/add', methods=['GET', 'POST'])
def addTrack(artist_id):
    if 'username' not in login_session:
        return redirect('/login')
    artist = session.query(Artist).filter_by(id=artist_id).one()
    if request.method == 'POST':
        newTrack = Track(
            title=request.form['title'], lyrics=request.form['lyrics'],
            video=request.form['video'], artist_id=artist_id,
            user_id=login_session['user_id'])
        session.add(newTrack)
        session.commit()
        flash("{} Successfully Added".format(newTrack.title))
        return redirect(url_for('showTracks', artist_name=artist.name))
    return render_template('addtrack.html', artist=artist)


# JSON API to view the catalog
@app.route('/catalog.json')
def artistsJSON():
    artists = session.query(Artist).all()
    # List of dictionaries(tracks_tup)
    artists_list = []
    for artist in artists:
        tracks = session.query(Track).filter_by(artist_id=artist.id).all()
        # Dictionary of one item (tracks, List_of_Tracks)
        tracks_dicc = artist.serialize
        # List of the tracks's dictionary
        tracks_listAux = []
        for track in tracks:
            tracks_listAux.append(track.serialize)
        tracks_dicc['Tracks'] = tracks_listAux
        artists_list.append(tracks_dicc)
    return jsonify(Artists=artists_list)


# JSON API to view the tracks for an artist
@app.route('/catalog/<string:artist_name>/JSON')
def tracksJSON(artist_name):
    artist = session.query(Artist).filter_by(name=artist_name).one()
    tracks = session.query(Track).filter_by(artist_id=artist.id).all()
    tracks_list = []
    for track in tracks:
        tracks_list.append(track.serialize)
    return jsonify(Tracks=tracks_list)


# JSON API to view an specify track
@app.route('/catalog/<string:artist_name>/<string:track_title>/JSON')
def trackJSON(artist_name, track_title):
    artist = session.query(Artist).filter_by(name=artist_name).one()
    track = session.query(Track).filter_by(
        artist_id=artist.id, title=track_title).one()
    return jsonify(Track=track.serialize)


if __name__ == '__main__':
    app.secret_key = '88040422507vryyo'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
