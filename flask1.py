from flask import Flask

'''
__name__ gives name of the file.
'''

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world!"

app.run(port=5000)

'''
****************************************  HTTP VERSB ********************************************************
GET   means to retrieve (browsers are always configured to use the get method)
POST  means receive data and use it
PUT   Make sure something is there  (if we are send data, if the item is not there it will create, else if it is there it will update it)
DELETE  Remove something
There are other types of HTTP verbs.
'''