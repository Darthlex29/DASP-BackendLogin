from app import db


class Client(db.Model):
    __tablename__ = 'Client'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    direction = db.Column(db.String(80), nullable=False)
    credit_card = db.Column(db.String(16))
    web_page = db.Column(db.String(200))
    pay_mode = db.Column(db.String(10))
    is_active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    # Relaciones
    tickets = db.relationship('Ticket', backref='Client', lazy=True)
    invoices = db.relationship('Invoice', backref='client', lazy=True)
    hostings = db.relationship('Hosting', backref='client', lazy=True)
    distributors = db.relationship('Distributor', backref='client', lazy=True)
    # domains = db.relationship('DomainVO', backref='client', lazy=True)

    def __init__(self, direction, credit_card, web_page, pay_mode, is_active=True, user_id=None):
        self.direction = direction
        self.credit_card = credit_card
        self.web_page = web_page
        self.pay_mode = pay_mode
        self.is_active = is_active
        self.user_id = user_id

    def to_JSON(self):
        return {
            'id': self.id,
            'direction': self.direction,
            'credit_card': self.credit_card,
            'web_page': self.web_page,
            'pay_mode': self.pay_mode,
            'is_active': self.is_active,
            'user_id': self.user_id
        }

    def from_JSON(self, data):
        for field in ['direction', 'credit_card', 'web_page', 'pay_mode', 'is_active', 'user_id']:
            if field in data:
                setattr(self, field, data[field])

    '''def from_JSON(self, data):
       for field in ['direction', 'credit_card', 'web_page', 'pay_mode', 'is_active']:
            if field in data:
                setattr(self, field, data[field])'''
