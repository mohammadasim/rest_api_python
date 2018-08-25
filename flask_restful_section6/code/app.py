from resources.user import UserRegister
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.item import Item, ItemList
import datetime
'''
The Api works with a resource and every resource needs to be a class
The class needs to inherit from Resource class. Once the class is defined 
it is added to the api as a resource
Important point is that in Flask Restful we don't have to use jsonify as that is done for us.
reqparse is a library that allows us to parse through the json payload received.
'''

app = Flask(__name__)
'''
Here we are turning off the Flask sqlalchemy tracker, but sqlalchemy itself has another tracker in the
main library and that one is better and which is on.
'''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)
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

#Config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
if __name__ == '__main__':
    '''
    The reason that we are importing db here is to avoid circular imports.
    our object models will also import db and we import up there our object models too and
    then db will alreadby be ther if we had imported it there.
    '''
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)