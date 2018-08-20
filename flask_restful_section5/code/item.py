import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import JWT, jwt_required
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
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}, 200
        return {'message': 'Item not found'}, 404
    @jwt_required()
    def post(self, name):
        '''
        Creates item
        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        item_check_query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(item_check_query, (name,))
        row = result.fetchone()
        if row:
            connection.close()
            return {'message': 'Item already exists'}, 400
        else:
            data = Item.parser.parse_args()
            create_item_query = "INSERT INTO items VALUES(?,?)"
            cursor.execute(create_item_query, (name, data['price']))
            connection.commit()
            connection.close()
        return {'item': {'name': name, 'price': data['price']}}, 201

    def delete(self, name):
        '''
        Deletes item
        '''
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        '''
        This method updates an item if it already exists otherwise it will create it.
        the update() method is dictionary method that updates the values with the values in data
        We have added requestparse it will parse through the payload and only collect the arguments that
        we have defined. This gives us more control over the updating of elements.
        '''
        data = Item.parser.parse_args()
        item = next(filter(lambda x : x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    '''
    Items resources, list of all items
    '''
    def get(self):
        '''
        get list of items.
        '''
        return{'items': items}