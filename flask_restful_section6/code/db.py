from flask_sqlalchemy import SQLAlchemy

'''
Below we initialise a SQLAlchemy object that is going to get linked to our APP.
This object will look up the object that we are going to allow it to look at in our app
and then map them to rows in the table.
'''

db = SQLAlchemy()