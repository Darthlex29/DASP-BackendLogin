from app import db

class DomainVO(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain_name = db.Column(db.String(100), nullable=False)
    #client_id = db.Column(db.Integer, db.ForeignKey('ClientVO.id'))

    def __init__(self, domain_name, client_id):
        self.domain_name = domain_name
        #self.client_id = client_id

    def to_JSON(self):
        return {
            'id': self.id,
            'domain_name': self.domain_name,
            #'client_id': self.client_id
        }

    '''def from_JSON(self, data):
        for field in ['domain_name', 'client_id']:
            if field in data:
                setattr(self, field, data[field])'''