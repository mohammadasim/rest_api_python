'''
We have moved some class methods from the item resource to this file. The reason being that a resource should have methods that 
the endpoints interact with them directly they should have only GET, PUT, POST, DELETE methods and not class methods.
Models are back end classes that are more like helper classes and are not visible through the API
'''

from db import db

class ItemModel(db.Model):
    '''
    With the inclusion of db.Model we are telling SQLAlchemy that this is model object that it has to map
    '''
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeighKey('stores.id'))
    store = db.relationship('StoreModel')


    def __init__(self, name, price):
            self.name = name
            self.price = price

    def json(self):
        '''
        Json representation of ItemModel
        '''
        return {'name': self.name, 'price': self.price}
    
    @classmethod
    def find_by_name(cls, name):
        '''
        We are now going to use sqlalchemy.
        The query object below if part of sqlalchemy and sqlalchemy will return an object to us.
        this library has helped us in getting rid of all the boilerplate code
        '''
        return cls.query.filter_by(name=name).first() #This is equal to Select * from items where name=name

    def save_to_db(self):
        '''
        session is an object that we use to add object to database.  We can add multiple objects to session
        and they will get added.
        When we are updating an item we add the updated item to session and that will then be committed. Hence
        there is no need for update method and we change the name of the method because it is not only inserting object
        but updating as well.
        '''
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        '''
        Deletes an existing item from db
        '''
        db.session.delete(self)
        db.session.commit()