from flask import Flask, jsonify, request, render_template

'''
__name__ gives name of the file.
Jsonify is a method in flask that converts data into json and thus can easily be sent across
request is used for getting data out that was received from the browser
'''

app = Flask(__name__)

stores = [
    {
        'name': 'My wonderful store',
        'items': [
            {
                'name' : 'My item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

#### APIs to Build ####
# POST /store data:{name}
# GET /store/<string:name>
# GET /store
# POST /store/<string:name>/item {name:, price:}
# GET /store/<string:name>/item

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()  #this method changes the json respond received into a dictionary
    new_store = {
        'name' : request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'message': 'Store not found'})


@app.route('/store')
def get_stores(): # Json is alway a dictionary of key value pairs
    return jsonify({'stores': stores}) #The problem is that our stores variable is a list and json can't be a list, so we change it into a dictionary

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    received_request = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : received_request['name'],
                'price': received_request['price']
            }
            store['items'].append(new_item)
            return jsonify({'items': store['items']})
        else:
            return jsonify({'message': "Couldn't locate the store"})

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        else:
            return jsonify({'message': 'Items not found'})


app.run(port=5000)

'''
****************************************  HTTP VERSB ********************************************************
GET   means to retrieve (browsers are always configured to use the get method)
POST  means receive data and use it
PUT   Make sure something is there  (if we are send data, if the item is not there it will create, else if it is there it will update it)
DELETE  Remove something
There are other types of HTTP verbs.
'''