from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    idDocument = db.Column(db.Integer, nullable=False)
    documentType = db.Column(db.String(80), nullable=False)

    #Relacion uno a uno con ClientVO
    client = db.relationship('Client', backref='User', lazy=True, uselist=False)
    #Relacion uno a uno con EmployeeVO
    employees = db.relationship('Employee', backref='User', lazy=True)

    def __init__(self, name, email, password, idDocument, documentType):
        self.name = name
        self.documentType = documentType
        self.idDocument = idDocument
        self.email = email
        self.password = password

    @classmethod
    def checkPassword(self, hashedPassword, password):
        return check_password_hash(hashedPassword, password)
    
    @classmethod
    def convertPassword(self, password):
        return generate_password_hash(password)
    
    def hashPassword(self):
        passw = self.convertPassword(self.password)
        self.password = passw  

    def to_JSON(self):
        return {
            'id':self.id,
            'name':self.name, 
            'documentType':self.documentType,
            'idDocument': self.idDocument,
            'email': self.email,
            'password': self.password
        }
    
    def from_JSON(self, data):
        for field in ['name', 'email', 'password', 'documentType', 'idDocument']:
            if field in data:
                setattr(self, field, data[field])



