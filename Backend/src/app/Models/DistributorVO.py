from app import db

class Distributor(db.Model):
    __tablename__ = 'Distributor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(10))
    client_id = db.Column(db.Integer, db.ForeignKey('Client.id'))

    def __init__(self, name, category, client_id):
        self.name = name
        self.category = category
        self.client_id = client_id

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'client_id': self.client_id
        }

    def from_JSON(self, data):
        for field in ['name', 'category', 'client_id']:
            if field in data:
                setattr(self, field, data[field])