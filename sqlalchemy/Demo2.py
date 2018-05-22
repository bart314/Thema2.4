#coding: utf-8
import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
        
conn = sqla.create_engine('mysql+pymysql://docent:hoppekee@localhost/demo?host=localhost?port=3306?charset=utf8')
Base = declarative_base()


class Artist(Base):
    __tablename__ = "artist"
    #Elk model moet een primaire sleutel bevatten, normalitair aangeduid met <tt>id</tt> 
    id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True)
    naam = sqla.Column('naam', sqla.String(64), nullable=False, unique=True, index=True)
    land = sqla.Column('land', sqla.String(2)) #ISO3166-1: tweeletterige weergave van het land
    taal = sqla.Column('taal', sqla.String(3)) #ISO639: drieletterige weergave van een taal
    liedje = relationship('Liedje', backref='Artist')


    def __repr__(self):
        return '<Artist %r>' % self.naam


class Liedje(Base):
    __tablename__ = "liedje" 
    id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True)
    titel = sqla.Column('titel', sqla.String(64), nullable=False, unique=True, index=True)
    lengte = sqla.Column('lengte', sqla.Integer) # lengte in seconden
    artist_id = sqla.Column(sqla.Integer, sqla.ForeignKey('artist.id'))


    def __repr__(self):
        return '<Liedje %r>' % self.titel

    '''
    Deze methode geeft een dictionary terug, die door eventuele clients 
    gebruikt kan worden om om te zetten in json. Het voordeel van een
    eigen implementatie is dat je meer controle hebt over het format en
    de data die teruggegeven wordt. Een dictionary heeft als voordeel dat 
    je data makkelijk aan elkaar kunt knopen (althans sinds Python3, zie
    http://stackoverflow.com/questions/38987/how-to-merge-two-python-dictionaries-in-a-single-expression#26853961
    '''

    def to_json(self):
        return {
          'titel': self.titel,
          'lengte': self.lengte
        }


class Persister():
    def __init__(self):
        Session = sessionmaker(bind=conn)
        self.session = Session()

    def get_titles(self, artist): 
         rv = session.query(Liedje).join(Artist, Liedje.artist_id==Artist.id).filter(Artist.naam=="Sonic Youth").all()
         return json.dumps(rv)

    
