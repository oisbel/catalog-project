from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, User, Artist, Track

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create user
user1 = User(name="Oisbel Simpson", email="oisbelsimpv@gmail.com")
session.add(user1)
session.commit()

# Tracks for Lauren Daigle
artist0 = Artist(
       name="Lauren Daigle",
       picture="https://image.ibb.co/fiYSQm/Lauren_Daigle.png")

session.add(artist0)
session.commit()

f = open("lyrics/Lauren Daigle-O' Lord.txt")
content = f.read()
f.close()
track0 = Track(
       title="O' Lord",
       lyrics=content,
       video="https://www.youtube.com/watch?v=eHp585tdIjQ",
       artist=artist0, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/Lauren Daigle-Trust In You.txt")
content = f.read()
f.close()
track1 = Track(
       title="Trust In You",
       lyrics=content,
       video="https://www.youtube.com/watch?v=n_aVFVveJNs",
       artist=artist0, user=user1)
session.add(track1)
session.commit()

f = open("lyrics/Lauren Daigle-How Can It Be.txt")
content = f.read()
f.close()
track2 = Track(
       title="How Can It Be",
       lyrics=content,
       video="https://www.youtube.com/watch?v=Wt5X91ciE6Y",
       artist=artist0, user=user1)
session.add(track2)
session.commit()

f = open("lyrics/Lauren Daigle-Come Alive (Dry Bones).txt")
content = f.read()
f.close()
track3 = Track(
       title="Come Alive (Dry Bones)",
       lyrics=content,
       video="https://www.youtube.com/watch?v=7XAeyFagceQ",
       artist=artist0, user=user1)
session.add(track3)
session.commit()

# Tracks for Hillsong Worship
artist1 = Artist(
       name="Hillsong Worship",
       picture="https://image.ibb.co/n2k7Qm/Hillsong_Worship.png")

session.add(artist1)
session.commit()

f = open("lyrics/Hillsong Worship-What A Beautiful Name.txt")
content = f.read()
f.close()
track0 = Track(
       title="What A Beautiful Name",
       lyrics=content,
       video="https://www.youtube.com/watch?v=nQWFzMvCfLE",
       artist=artist1, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/Hillsong Worship-Here I Am To Worship.txt")
content = f.read()
f.close()
track1 = Track(
       title="Here I Am To Worship",
       lyrics=content,
       video="https://www.youtube.com/watch?v=6CKCThJB5w0",
       artist=artist1, user=user1)
session.add(track1)
session.commit()

# Tracks for Chris tomlin
artist2 = Artist(
       name="Chris tomlin",
       picture="https://image.ibb.co/ch4Z5m/Chris_tomlin.png")

session.add(artist2)
session.commit()

f = open("lyrics/Chris tomlin-Our God.txt")
content = f.read()
f.close()
track0 = Track(
       title="Our God",
       lyrics=content,
       video="https://www.youtube.com/watch?v=NJpt1hSYf2o",
       artist=artist2, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/Chris tomlin-How Great Is Our God.txt")
content = f.read()
f.close()
track1 = Track(
       title="How Great Is Our God",
       lyrics=content,
       video="https://www.youtube.com/watch?v=KBD18rsVJHk",
       artist=artist2, user=user1)
session.add(track1)
session.commit()

# Tracks for Casting Crowns
artist3 = Artist(
       name="Casting Crowns",
       picture="https://image.ibb.co/j3fkBR/Casting_Crowns.png")

session.add(artist3)
session.commit()

f = open("lyrics/Casting Crowns-Who Am I.txt")
content = f.read()
f.close()
track0 = Track(
       title="Who Am I",
       lyrics=content,
       video="https://www.youtube.com/watch?v=mBcqria2wmg",
       artist=artist3, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/Casting Crowns-Oh My Soul.txt")
content = f.read()
f.close()
track1 = Track(
       title="Oh My Soul",
       lyrics=content,
       video="https://www.youtube.com/watch?v=Tn5aq54yu8A",
       artist=artist3, user=user1)
session.add(track1)
session.commit()

f = open("lyrics/Casting Crowns-Praise You In This Storm.txt")
content = f.read()
f.close()
track2 = Track(
       title="Praise You In This Storm",
       lyrics=content,
       video="https://www.youtube.com/watch?v=ohLfJDKSv0U",
       artist=artist3, user=user1)
session.add(track2)
session.commit()

# Tracks for MercyMe
artist4 = Artist(
       name="MercyMe",
       picture="https://image.ibb.co/fk63y6/MercyMe.png")

session.add(artist4)
session.commit()

f = open("lyrics/MercyMe-Even If.txt")
content = f.read()
f.close()
track0 = Track(
       title="Even If",
       lyrics=content,
       video="https://www.youtube.com/watch?v=B6fA35Ved-Y",
       artist=artist4, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/MercyMe-I Can Only Imagine.txt")
content = f.read()
f.close()
track1 = Track(
       title="I Can Only Imagine",
       lyrics=content,
       video="https://www.youtube.com/watch?v=N_lrrq_opng",
       artist=artist4, user=user1)
session.add(track1)
session.commit()

f = open("lyrics/MercyMe-Greater.txt")
content = f.read()
f.close()
track2 = Track(
       title="Greater",
       lyrics=content,
       video="https://www.youtube.com/watch?v=GXI0B4iMLuU",
       artist=artist4, user=user1)
session.add(track2)
session.commit()

# Tracks for for KING & COUNTRY
artist5 = Artist(
       name="For KING & COUNTRY",
       picture="https://image.ibb.co/kPXnQm/For_KING_COUNTRY.png")

session.add(artist5)
session.commit()

f = open("lyrics/For KING & COUNTRY-Shoulders.txt")
content = f.read()
f.close()
track0 = Track(
       title="Shoulders",
       lyrics=content,
       video="https://www.youtube.com/watch?v=TfiYWaeAcRw",
       artist=artist5, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/For KING & COUNTRY-O God Forgive Us.txt")
content = f.read()
f.close()
track1 = Track(
       title="O God Forgive Us",
       lyrics=content,
       video="https://www.youtube.com/watch?v=tz4toSf-xQU",
       artist=artist5, user=user1)
session.add(track1)
session.commit()

f = open("lyrics/For KING & COUNTRY-The Proof Of Your Love.txt")
content = f.read()
f.close()
track2 = Track(
       title="The Proof Of Your Love",
       lyrics=content,
       video="https://www.youtube.com/watch?v=b-2dKOfbC9c",
       artist=artist5, user=user1)
session.add(track2)
session.commit()

f = open("lyrics/For KING & COUNTRY-It's Not Over Yet.txt")
content = f.read()
f.close()
track3 = Track(
       title="It's Not Over Yet",
       lyrics=content,
       video="https://www.youtube.com/watch?v=XmTmTMcdxOs",
       artist=artist5, user=user1)
session.add(track3)
session.commit()

# Tracks for Danny Gokey
artist6 = Artist(
       name="Danny Gokey",
       picture="https://image.ibb.co/hveCrR/Danny_Gokey.png")

session.add(artist6)
session.commit()

f = open("lyrics/Danny Gokey-Tell Your Heart to Beat Again.txt")
content = f.read()
f.close()
track0 = Track(
       title="Tell Your Heart to Beat Again",
       lyrics=content,
       video="https://www.youtube.com/watch?v=PkdkiuJgqxk",
       artist=artist6, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/Danny Gokey-The Comeback.txt")
content = f.read()
f.close()
track1 = Track(
       title="The Comeback",
       lyrics=content,
       video="https://www.youtube.com/watch?v=Qvr64VsNT-s",
       artist=artist6, user=user1)
session.add(track1)
session.commit()

# Tracks for skillet
artist7 = Artist(
       name="Skillet",
       picture="https://image.ibb.co/jAXyWR/Skillet.png")

session.add(artist7)
session.commit()

f = open("lyrics/Skillet-Hero.txt")
content = f.read()
f.close()
track0 = Track(
       title="Hero",
       lyrics=content,
       video="https://www.youtube.com/watch?v=uGcsIdGOuZY",
       artist=artist7, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/Skillet-Rise.txt")
content = f.read()
f.close()
track1 = Track(
       title="Rise",
       lyrics=content,
       video="https://www.youtube.com/watch?v=b3jQ0tFqG_0",
       artist=artist7, user=user1)
session.add(track1)
session.commit()

f = open("lyrics/Skillet-Awake and Alive.txt")
content = f.read()
f.close()
track2 = Track(
       title="Awake and Alive",
       lyrics=content,
       video="https://www.youtube.com/watch?v=2aJUnltwsqs",
       artist=artist7, user=user1)
session.add(track2)
session.commit()

f = open("lyrics/Skillet-The Resistance.txt")
content = f.read()
f.close()
track3 = Track(
       title="The Resistance",
       lyrics=content,
       video="https://www.youtube.com/watch?v=vCWmHbpD0fE",
       artist=artist7, user=user1)
session.add(track3)
session.commit()

# Tracks for Hillary Scott & The Scott Family
artist8 = Artist(
       name="Hillary Scott & The Scott Family",
       picture="https://image.ibb.co/hjr3y6/Hillary_Scott_The_Scott_Family.png")   # NOQA

session.add(artist8)
session.commit()

f = open("lyrics/Hillary Scott & The Scott Family-Thy Will.txt")
content = f.read()
f.close()
track0 = Track(
       title="Thy Will",
       lyrics=content,
       video="https://www.youtube.com/watch?v=Dp4WC_YZAuw",
       artist=artist8, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/Hillary Scott & The Scott Family-Untitled Hymn.txt")
content = f.read()
f.close()
track1 = Track(
       title="Untitled Hymn",
       lyrics=content,
       video="https://www.youtube.com/watch?v=mVCUbJ_f16k",
       artist=artist8, user=user1)
session.add(track1)
session.commit()

# Tracks for NF
artist9 = Artist(
       name="NF",
       picture="https://image.ibb.co/nEAVd6/NF.png")

session.add(artist9)
session.commit()

f = open("lyrics/NF-Outcast.txt")
content = f.read()
f.close()
track0 = Track(
       title="Outcast",
       lyrics=content,
       video="https://www.youtube.com/watch?v=J7MYJ8Kxhwc",
       artist=artist9, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/NF-Let You Down.txt")
content = f.read()
f.close()
track1 = Track(
       title="Let You Down",
       lyrics=content,
       video="https://www.youtube.com/watch?v=0501BTnbrxg",
       artist=artist9, user=user1)
session.add(track1)
session.commit()

# Tracks for jordan feliz
artist10 = Artist(
       name="Jordan Feliz",
       picture="https://image.ibb.co/iKkVd6/Jordan_Feliz.png")

session.add(artist10)
session.commit()

f = open("lyrics/Jordan Feliz-The River.txt")
content = f.read()
f.close()
track0 = Track(
       title="The River",
       lyrics=content,
       video="https://www.youtube.com/watch?v=maT4phfTXR4",
       artist=artist10, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/Jordan Feliz-Beloved.txt")
content = f.read()
f.close()
track1 = Track(
       title="Beloved",
       lyrics=content,
       video="https://www.youtube.com/watch?v=pgJFUW3VenY",
       artist=artist10, user=user1)
session.add(track1)
session.commit()

f = open("lyrics/Jordan Feliz-Never Too Far Gone.txt")
content = f.read()
f.close()
track2 = Track(
       title="Never Too Far Gone",
       lyrics=content,
       video="https://www.youtube.com/watch?v=TG6s8DxQJ5w",
       artist=artist10, user=user1)
session.add(track2)
session.commit()

f = open("lyrics/Jordan Feliz-Best Of Me.txt")
content = f.read()
f.close()
track3 = Track(
       title="Best Of Me",
       lyrics=content,
       video="https://www.youtube.com/watch?v=9DV9dPMdBu4",
       artist=artist10, user=user1)
session.add(track3)
session.commit()

# Tracks for tobyMac
artist11 = Artist(
       name="TobyMac",
       picture="https://image.ibb.co/nnA7Qm/TobyMac.png")

session.add(artist11)
session.commit()

f = open("lyrics/TobyMac-Lights Shine Bright.txt")
content = f.read()
f.close()
track0 = Track(
       title="Lights Shine Bright",
       lyrics=content,
       video="https://www.youtube.com/watch?v=d17hi1s6Tgg",
       artist=artist11, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/TobyMac-Feel It.txt")
content = f.read()
f.close()
track1 = Track(
       title="Feel It",
       lyrics=content,
       video="https://www.youtube.com/watch?v=O8xGaE4S2gk",
       artist=artist11, user=user1)
session.add(track1)
session.commit()

f = open("lyrics/TobyMac-Speak Life.txt")
content = f.read()
f.close()
track2 = Track(
       title="Speak Life",
       lyrics=content,
       video="https://www.youtube.com/watch?v=ZeBv9r92VQ0",
       artist=artist11, user=user1)
session.add(track2)
session.commit()

f = open("lyrics/TobyMac-City On Our Knees.txt")
content = f.read()
f.close()
track3 = Track(
       title="City On Our Knees",
       lyrics=content,
       video="https://www.youtube.com/watch?v=v9XyAMnSh6g",
       artist=artist11, user=user1)
session.add(track3)
session.commit()

# Tracks for Matthew West
artist12 = Artist(
       name="Matthew West",
       picture="https://image.ibb.co/jiXbJ6/Matthew_West.png")

session.add(artist12)
session.commit()

f = open("lyrics/Matthew West-Broken Things.txt")
content = f.read()
f.close()
track0 = Track(
       title="Broken Things",
       lyrics=content,
       video="https://www.youtube.com/watch?v=WdUu6ZsdVfM",
       artist=artist12, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/Matthew West-Hello, My Name Is.txt")
content = f.read()
f.close()
track1 = Track(
       title="Hello, My Name Is",
       lyrics=content,
       video="https://www.youtube.com/watch?v=ZuJWQzjfU3o",
       artist=artist12, user=user1)
session.add(track1)
session.commit()

# Tracks for Francesca Battistelli
artist13 = Artist(
       name="Francesca Battistelli",
       picture="https://image.ibb.co/naW3y6/Francesca_Battistelli.png")

session.add(artist13)
session.commit()

f = open("lyrics/Francesca Battistelli-He Knows My Name.txt")
content = f.read()
f.close()
track0 = Track(
       title="He Knows My Name",
       lyrics=content,
       video="https://www.youtube.com/watch?v=jYpBgJHmGmw",
       artist=artist13, user=user1)
session.add(track0)
session.commit()

f = open("lyrics/Francesca Battistelli-Write Your Story.txt")
content = f.read()
f.close()
track1 = Track(
       title="Write Your Story",
       lyrics=content,
       video="https://www.youtube.com/watch?v=ecV1NHmELuA",
       artist=artist13, user=user1)
session.add(track1)
session.commit()

f = open("lyrics/Francesca Battistelli-Giants Fall.txt")
content = f.read()
f.close()
track2 = Track(
       title="Giants Fall",
       lyrics=content,
       video="https://www.youtube.com/watch?v=KtE-_1cwH1M&list",
       artist=artist13, user=user1)
session.add(track2)
session.commit()

f = open("lyrics/Francesca Battistelli-Free To Be Me.txt")
content = f.read()
f.close()
track3 = Track(
       title="Free To Be Me",
       lyrics=content,
       video="https://www.youtube.com/watch?v=EKSQjSdU8VA",
       artist=artist13, user=user1)
session.add(track3)
session.commit()

f = open("lyrics/Francesca Battistelli-Beautiful, Beautiful.txt")
content = f.read()
f.close()
track4 = Track(
       title="Beautiful, Beautiful", lyrics=content,
       video="https://www.youtube.com/watch?v=WB5BlYsn6nk",
       artist=artist13, user=user1)
session.add(track4)
session.commit()

print "Added Items!"
