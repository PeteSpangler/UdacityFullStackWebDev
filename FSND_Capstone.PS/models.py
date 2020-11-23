
import os
from sqlalchemy import Column, String, Integer, Float, DateTime, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

#database_path = 'postgres://peter:postgres@localhost:5432/stats'
database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

class Skaters(db.Model):
    __tablename__ = 'Skaters'

    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    pos = Column(String(20))
    pts = Column(Integer)
    gls = Column(Integer)

    def __repr__(self):
        return f'<Skaters {self.id}, {self.name} {self.pos}, {self.pts}, {self.gls}>'
   
    def __init__(self, name, pos, pts, gls):
        self.name = name
        self.pos = pos
        self.pts = pts
        self.gls = gls

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def short(self):
        return {
            'id': self.id,
            'name': self.name
            }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'pos': self.pos,
            'pts': self.pts,
            'gls': self.gls
            }
   
class Goalies(db.Model):
    __tablename__ = 'Goalies'

    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    gaa = Column(Float)
    so = Column(Integer)
    w = Column(Integer)

    def __init__(self, name, gaa, so, w):
        self.name = name
        self.gaa = gaa
        self.so = so
        self.w = w

    def __repr__(self):
        return f'<Goalies {self.gaa}, {self.so}, {self.w}>'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def short(self):
        return {
            'id': self.id,
            'name': self.name
            }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'gaa': self.gaa,
            'so': self.so,
            'w': self.w
            }