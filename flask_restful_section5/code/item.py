import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
class Item(Resource):
    '''
    Item resource
    '''
    parser = reqparse.RequestParser() #This initializes a new parser that we can use to parse a request.
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank") # Here we add arguments to the parser. We will then run the request through the parser and it will look for the argument added to the parser. 

    @jwt_required()
    def get(self, name):
        '''
        Retrieves item from the database
        '''
        item = Item.find_by_name(name)
        if item:
            return item     
        return {'message': 'Item not found'}, 404
        
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}, 200

    @jwt_required()
    def post(self, name):
        '''
        Creates item
        '''
        row = Item.find_by_name(name)
        if row:
            return {'message': "An Item by name '{}' already exists".format(name)}, 400
        else:
            data = Item.parser.parse_args()
            item = {'name': name, "price": data['price']}
            try:
                Item.insert_item(item)
            except:
                return {'message': 'An error occured inserting the item'}, 500
        return item, 201
    @classmethod
    def insert_item(cls, item):
        '''
        class method for inserting item to database
        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        create_item_query = "INSERT INTO items VALUES(?,?)"
        cursor.execute(create_item_query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    def delete(self, name):
        '''
        Deletes item
        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message': 'Item deleted'}
    @classmethod
    def update_item(cls, item):
        '''
        Updates an existing item
        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        update_query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(update_query, (item['price'], item['name']))
        connection.commit()
        connection.close()

    @jwt_required()
    def put(self, name):
        '''
        This method updates an item if it already exists otherwise it will create it.
        the update() method is dictionary method that updates the values with the values in data
        We have added requestparse it will parse through the payload and only collect the arguments that
        we have defined. This gives us more control over the updating of elements.
        '''
        item_exists = Item.find_by_name(name)
        data = Item.parser.parse_args()
        updated_item = {'name': name, "price": data['price']}
        if item_exists:
            try:
                Item.update_item(updated_item)
            except:
                {'message': 'An error occured while updating item in database'}, 500
        else:
            try:
                Item.insert_item(updated_item)
            except:
                return {'message': 'An error occured while inserting the item to database'}, 500
        return update_item


class ItemList(Resource):
    '''
    Items resources, list of all items
    '''
    def get(self):
        '''
        get list of items.
        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        row = cursor.execute(query)
        data = row.fetchall()
        connection.close()
        return {'item': data}