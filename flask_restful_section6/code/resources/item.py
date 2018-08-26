'''
Item resource
'''
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    '''
    Item resource
    '''
    #This initializes a new parser that we can use to parse a request.
    parser = reqparse.RequestParser() 
    parser.add_argument('price',
        type=float,
        required=True,
        #Here we add arguments to the parser. We will then run the request through the parser and it will look for the argument added to the parser. 
        help="This field cannot be left blank")

    @jwt_required()
    def get(self, name):
        '''
        Retrieves item from the database
        '''
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404   
    @jwt_required()
    def post(self, name):
        '''
        Creates item
        '''
        row = ItemModel.find_by_name(name)
        if row:
            return {'message': "An Item by name '{}' already exists".format(name)}, 400
        else:
            data = Item.parser.parse_args()
            item = ItemModel(name, data['price'])
            try:
                item.save_to_db()
            except:
                return {'message': 'An error occured inserting the item'}, 500
        return item.json(), 201

    def delete(self, name):
        '''
        Deletes item
        '''
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted'}
        else:
            return {'message': 'Item not deleted as not present in db'}

    @jwt_required()
    def put(self, name):
        '''
        This method updates an item if it already exists otherwise it will create it.
        the update() method is dictionary method that updates the values with the values in data
        We have added requestparse it will parse through the payload and only collect the arguments that
        we have defined. This gives us more control over the updating of elements.
        '''
        item_exists = ItemModel.find_by_name(name)
        data = Item.parser.parse_args()
        updated_item = ItemModel(name, data['price'])
        if item_exists:
            try:
                updated_item.update_item()
            except:
                {'message': 'An error occured while updating item in database'}, 500
        else:
            try:
                updated_item.insert_item()
            except:
                return {'message': 'An error occured while inserting the item to database'}, 500
        return updated_item.json()


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