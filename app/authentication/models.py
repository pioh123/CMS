from app import db
from itsdangerous import (TimedJSONWebSignatureSerializer
                             as Serializer, BadSignature, SignatureExpired)

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,
                              default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class User(Base):

    __tablename__ = 'auth_user'

    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    email    = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    def generate_token(self, expiration = 700):
        s = Serializer('key_word')
        return s.dumps({'id': self.id, 'username':self.username, 'email':self.email})
    

    def __init__(self, name, email, password):

        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)
