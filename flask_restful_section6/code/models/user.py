import sqlite3
from db import db
class UserModel(db.Model):
    '''
    Below we are telling SQLAlchemy the table it has to use and the columns.
    We can define object variables in the __init__ method of the object but if we will not map them like below
    the values of those variables will not be saved and it won't give an error either.
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        '''
        Adds userModel to database
        '''
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_username(cls, username ):
        
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id ):
        return cls.query.filter_by(id=_id).first()