from model.area import AreaModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Area(Resource):
    pareser = reqparse.RequestParser()
    pareser.add_argument('name', 
    type = str,
    required = True,
    help = 'Area name is required')

    @jwt_required()
    def get(self, name):
        area = AreaModel.search_area_byname(name)
        if area:
            return area.json(), 200
        else:
            return {'message': 'Area not found'}, 404
    
    @jwt_required()
    def put(self, name):
        area = AreaModel.search_area_byname(name)
        if area:
            return {'message': 'Aread already exists'}, 404
        else:
            area = AreaModel(name)
            area.save_to_db()
            return area.json()

    @jwt_required()
    def delete(self,name):
        area = AreaModel.search_area_byname(name)
        if area:
            area.delete()
            return {'message':"Area with name '{}' deleted".format(name)}, 204
        else:
            return {'message': 'Wrong area name provided'}, 404

class AreaList(Resource):
    @jwt_required()
    def get(self):
        return(list[map(lambda x: x.json() for x in StoreMode.query.all())])