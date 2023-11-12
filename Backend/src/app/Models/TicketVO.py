from app import db

class Ticket(db.Model):
    __tablename__ = 'Ticket'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    state = db.Column(db.String(10), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('Client.id'))
    
    def __init__(self, description, state, client_id):
        self.description = description
        self.state = state
        self.client_id = client_id

    def to_JSON(self):
        return {
            'id': self.id,
            'description': self.description,
            'state': self.state,
            'client_id': self.client_id
        }

    def from_JSON(self, data):
        for field in ['description', 'state', 'client_id']:
            if field in data:
                setattr(self, field, data[field])