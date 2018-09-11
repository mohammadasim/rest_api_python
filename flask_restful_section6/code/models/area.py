from db import db

class AreaModel(db.Model):
    __tablename__ = "area"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.str)
    stores = db.relationship('StoreModel', lazy = 'dynamic')

    def __init__(self, name):
        self.name = name

    def json():
        return {'name': self.name, 'stores': list[map(lambda x: x.json() for x in stores)]}
    @classmethod
    def search_area_byname(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.commit()



