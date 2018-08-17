from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
'''
The Api works with a resource and every resource needs to be a class
The class needs to inherit from Resource class. Once the class is defined 
it is added to the api as a resource
Important point is that in Flask Restful we don't have to use jsonify as that is done for us.
reqparse is a library that allows us to parse through the json payload received.
'''

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
items = []
'''
JWT is a library that is used for authentication. It gives us a default endpoint /auth.
with /auth we send username and password. JWT returns us an authorization token.
We then send that authorisation token in the request header with key authorization and value JWT (space) then 
followed by the access token.
This header is required for methods that have decorator @jwt_required()
When we send the authorization token jwt decrypts it and extract the user id from it.
it then calls the identity method and using the user id retreives the user.
It checks the username and password with user it has retreived and then if the user exists
and the username and password matches it allows the function to takes place.
'''
jwt = JWT(app, authenticate, identity) # /auth
class Item(Resource):
    '''
    Item resource
    '''
    @jwt_required()
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
        '''
        Creates item
        '''
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'An item with name {} already exists.'.format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

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
        parser = reqparse.RequestParser() #This initializes a new parser that we can use to parse a request.
        parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be left blank") # Here we add arguments to the parser. We will then run the request through the parser and it will look for the argument added to the parser. 

        data = parser.parse_args()
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

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)