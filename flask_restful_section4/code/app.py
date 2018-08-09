from flask import Flask, request
from flask_restful import Resource, Api
'''
The Api works with a resource and every resource needs to be a class
The class needs to inherit from Resource class. Once the class is defined 
it is added to the api as a resource
Important point is that in Flask Restful we don't have to use jsonify as that is done for us.
'''

app = Flask(__name__)
api = Api(app)
items = []

class Item(Resource):
    def get(self, name):
        '''
        The filter functions takes two parameters, a lambda function and an iterable which is 
        the list item. Filter will filter all those objects for which the function in this case
        the lambda function will return true.
        The filter will return a list and we can then call the builtin next() to get the next item
        next() will throw exception if there isn't another item, hence we use a default value none
        '''
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item is not None else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'An item with name '{}' already exists.'.format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201
class ItemList(Resource):
    def get(self):
        return{'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)