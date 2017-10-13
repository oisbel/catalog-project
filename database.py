from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Artist(Base):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Track(Base):
    __tablename__ = 'track'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    lyrics = Column(String(250), nullable=False)
    video = Column(String(250))
    artist_id = Column(Integer, ForeignKey('artist.id'))
    artist = relationship(Artist)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'artist_id': self.artist_id,
            'lyrics': self.lyrics,
            'id': self.id,
            'title': self.title,
        }


engine = create_engine('sqlite:///catalog.db')


Base.metadata.create_all(engine)