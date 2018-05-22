#coding: utf-8
import json
from Demo2 import conn,Artist,Liedje,Base
from sqlalchemy.orm import sessionmaker

# to start with a clean sheet
Base.metadata.drop_all(conn)
Base.metadata.create_all(conn)

Session = sessionmaker(bind=conn)
session = Session()

a1 = Artist(naam="Sting", land="UK", taal="eng")
a2 = Artist(naam="Steen", land="NL", taal="nld")
a3 = Artist(naam="Sonic Youth", land="US", taal="eng")
a4 = Artist(naam="Boy", land="US", taal="eng")

for a in [a1,a2,a3,a4]:
    session.add(a)

session.commit()


l1 = Liedje(titel="Russians", lengte=201, artist_id=a1.id)
l2 = Liedje(titel="Moon over Bourbon street", lengte=420, artist_id=a1.id)
l3 = Liedje(titel="Vocking Steenwaren", lengte=502, artist_id=a2.id)
l4 = Liedje(titel="Morsdood", lengte=320, artist_id=a2.id)
l5 = Liedje(titel="Kotton Krown", lengte=453, artist_id=a3.id)
l6 = Liedje(titel="Tunic", lengte=533, artist_id=a3.id)
l7 = Liedje(titel="Candle", lengte=463, artist_id=a3.id)
l8 = Liedje(titel="Fear", lengte=374, artist_id=a4.id)
l9 = Liedje(titel="Into the Wild", lengte=320, artist_id=a4.id)

for l in [l1,l2,l3,l4,l5,l6,l7,l8,l9]:
    session.add(l)

session.commit();


# Alle liedjes van Sonic Youth
foo = session.query(Liedje).join(Artist, Liedje.artist_id==Artist.id).filter(Artist.naam=="Sonic Youth").all()
print (foo)

# maar dat is niet zo interessant. Beter is om de to_json-methode van het liedje aan te roepen.
for l in foo:
    print(l.to_json())


# als we die allemaal in één json-object gerepresenteerd willen zien, kun je het onderstaande gebruiken:
rv = []
for l in foo:
    rv.append(l.to_json())

print(json.dumps(rv))
