from app import db

class Hosting(db.Model):
    __tablename__ = 'Hosting'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hosting_name = db.Column(db.String(50), nullable=False)
    is_free = db.Column(db.Boolean)
    client_id = db.Column(db.Integer, db.ForeignKey('Client.id'))

    def __init__(self, hosting_name, is_free, client_id):
        self.hosting_name = hosting_name
        self.is_free = is_free
        self.client_id = client_id

    def to_JSON(self):
        return {
            'id': self.id,
            'hosting_name': self.hosting_name,
            'is_free': self.is_free,
            'client_id': self.client_id
        }

    def from_JSON(self, data):
        for field in ['hosting_name', 'is_free', 'client_id']:
            if field in data:
                setattr(self, field, data[field])