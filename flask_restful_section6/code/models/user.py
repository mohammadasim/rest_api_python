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

    def __init__(self, _id, username, password):
        '''
        We are using _id instead of id as id is a python key word
        '''
        self.id = _id
        self.username = username
        self.password = password
    '''    
    @classmethod
    def db_connection():
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        return cursor
    '''
    @classmethod
    def find_by_username(cls, username ):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        select_query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(select_query, (username,)) # The only way to pass a parameter, it has to be in the form of a tuple.
        # the username is the form of a single tuple
        row = result.fetchone() # fetchone() is a method of cursor object
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id ):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        select_query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(select_query, (_id,)) # The only way to pass a parameter, it has to be in the form of a tuple.
        # the username is the form of a single tuple
        row = result.fetchone() # fetchone() is a method of cursor object
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user