#coding: utf-8

from Demo1 import conn,Artist
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

def clear_table(s):
    for a in s.query(Artist).all():
        s.delete(a)

    s.commit()

Session = sessionmaker(bind=conn)
session = Session()
clear_table(session)

# C R E A T E
# Aanmaken van data
a1 = Artist(naam="Sting", land="UK", taal="eng")
a2 = Artist(naam="Nek", land="IT", taal="ita")
a3 = Artist(naam="Steen", land="NL", taal="nld")
a4 = Artist(naam="Brainpower", land="NL", taal="nld")
a5 = Artist(naam="Sonic Youth", land="US", taal="eng")
a6 = Artist(naam="Anderson Paak", land="NL", taal="nld")
a7 = Artist(naam="Boy", land="US", taal="eng")
a8 = Artist(naam="Cage the Elephant", land="US", taal="eng")
a9 = Artist(naam="Jacques Brel", land="FR", taal="fra")

for a in [a1,a2,a3,a4,a5,a6,a7,a8,a9]:
    session.add(a)

session.commit()

# R E A D 
# Opvragen van data uit de database:
foo = session.query(Artist).filter(Artist.land=="NL")  # let op: dubbele ==, want je bent niet met sql bezig
for a in foo:
    print (a)


# U P D A T E 
# Natuurlijk werkt een update ook gewoon
foo = session.query(Artist).filter(Artist.naam=="Sting").first() # foo is nu een Artist (duck typing)
foo.naam="Gordon Sumner"
session.commit();


# D E L E T E
# Verwijderen van data
# Zie voor die parameter in delete: http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.delete
foo = session.query(Artist).filter(Artist.naam=="Nek")
foo.delete(synchronize_session=False)
session.commit()


# Dit kan natuurlijk complexer worden
foo = session.query(Artist.naam, Artist.taal).filter(Artist.naam.like("%St%"))
for a in foo:
    print ("Naam: {}, taal: {}".format( a.naam, a.taal))



#Invoegen van dubbele naam gaat niet, dus dat moet je afvangen
a10 = Artist(naam="Steen", land="NL", taal="nld")
try:
    session.add(a10)
    session.commit()
except IntegrityError:
    print ("Dubbele entry")


