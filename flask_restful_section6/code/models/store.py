from db import db

class StoreModel(db.Model):
    '''
    With the inclusion of db.Model we are telling SQLAlchemy that this is model object that it has to map
    '''
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))


    def __init__(self, name):
            self.name = name

    def json(self):
        '''
        Json representation of StoreModel
        '''
        return {'name': self.name, 'items': self.items}
    
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