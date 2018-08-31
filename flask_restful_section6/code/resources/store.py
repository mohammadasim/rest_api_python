
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):
    '''
    Item resource
    '''

    @jwt_required()
    def get(self, name):
        '''
        Retrieves store from the database
        '''
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404   

    @jwt_required()
    def post(self, name):
        '''
        Creates store
        ''' 
        if StoreModel.find_by_name(name):
            return {'message': "A Store by name '{}' already exists".format(name)}, 400
        else:
            store = StoreModel(name)
            try:
                store.save_to_db()
            except:
                return {'message': 'An error occured inserting the store to db'}, 500
        return store.json(), 201

    def delete(self, name):
        '''
        Deletes store
        '''
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Store deleted'}
        else:
            return {'message': 'Store not deleted as not present in db'}

class StoreList(Resource):
    @jwt_required
    def get(self):
        return []
