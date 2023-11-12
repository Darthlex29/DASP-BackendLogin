from app import db

class Invoice(db.Model):
    __tablename__ = 'Invoice'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(20), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('Client.id'))

    def __init__(self, invoice_type, client_id):
        self.type = invoice_type
        self.client_id = client_id

    def to_JSON(self):
        return {
            'id': self.id,
            'type': self.type,
            'client_id': self.client_id
        }

    def from_JSON(self, data):
        for field in ['type', 'client_id']:
            if field in data:
                setattr(self, field, data[field])