'''
We have moved some class methods from the item resource to this file. The reason being that a resource should have methods that 
the endpoints interact with them directly they should have only GET, PUT, POST, DELETE methods and not class methods.
Models are back end classes that are more like helper classes and are not visible through the API
'''
import sqlite3

class ItemModel():
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
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return cls(*row)

    def insert_item(self):
        '''
        class method for inserting item to database
        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        create_item_query = "INSERT INTO items VALUES(?,?)"
        cursor.execute(create_item_query, (self.name, self.price))
        connection.commit()
        connection.close()
    
    def update_item(self):
        '''
        Updates an existing item
        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        update_query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(update_query, (self.price, self.name))
        connection.commit()
        connection.close()