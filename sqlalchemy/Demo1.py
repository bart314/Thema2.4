#coding: utf-8
import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
        
conn = sqla.create_engine('mysql+pymysql://docent:hoppekee@localhost/demo?host=localhost?port=3306?charset=utf8')

'''
<tt>declarative_base</tt> is een factory die een basis-klasse teruggeeft di
vervolgens de basis vormt voor al onze gepersisteerde klassen. 
Dit zijn allemaal <i>declarative classes</i>: klassen die bedoeld 
zijn om datatypen te <i>declareren</i> (definiëren).
'''

Base = declarative_base()


'''
Dit is het model. In de context van ORM is het model feitelijk 
een klasse die velden heeft die corresponderen met de attributen
(kolommen) van de tabel die door het object wordt gerepresenteerd.
'''

class Artist(Base):
    __tablename__ = "artist"
    #Elk model moet een primaire sleutel bevatten, normalitair aangeduid met <tt>id</tt> 
    id = sqla.Column('id', sqla.Integer, primary_key=True, autoincrement=True)
    naam = sqla.Column('naam', sqla.String(64), nullable=False, unique=True, index=True)
    land = sqla.Column('land', sqla.String(2)) #ISO3166-1: tweeletterige weergave van het land
    taal = sqla.Column('taal', sqla.String(3)) #ISO639: drieletterige weergave van een taal

    '''
    De methode <tt>__repr__</tt> is niet noodzakelijk, maar het is wel gebruikelijk om deze 
    te implementeren. Dit geeft een tekstuele representatie terug van het object in kwestie
    (vergelijkbaar met <tt>toString()</tt> in Java).
    '''

    def __repr__(self):
        return '<Artist %r>' % self.naam



#Aanmaken van de tabel
Base.metadata.create_all(conn)


