from flask import Flask
from flask_restful import Resource, Api
'''
The Api works with a resource and every resource needs to be a class
The class needs to inherit from Resource class. Once the class is defined 
it is added to the api as a resource
'''

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name):
        return {'student': name}

api.add_resource(Student, '/student/<string:name>')

app.run(port=5000)