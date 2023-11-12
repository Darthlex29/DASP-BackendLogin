from app import db

class Employee(db.Model):
    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rol = db.Column(db.String(20), nullable=False)
    is_hire = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    def __init__(self, rol, is_hire=True, user_id=None):
        self.rol = rol
        self.is_hire = is_hire
        self.user_id = user_id

    def to_JSON(self):
        return {
            'id': self.id,
            'is_hire': self.is_hire,
            'rol': self.rol
        }

    def from_JSON(self, data):
        for field in ['is_hire', 'rol']:
            if field in data:
                setattr(self, field, data[field])

'''class EmployeeVO(db.Model):

    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rol = db.Column(db.String(20), nullable=False)
    is_hire = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

        #self.hire_date = hire_date if hire_date is not None else datetime.utcnow()
    def __init__(self, rol, is_hire=True, user_id=None):
        self.rol = rol
        self.is_hire = is_hire
        self.user_id = user_id

    def __init__(self, rol, is_hire=True):
        #self.hire_date = hire_date if hire_date is not None else datetime.utcnow()
        self.rol = rol
        self.is_hire = is_hire

    def to_JSON(self):
        return {
            'id': self.id,
            #'hire_date': self.hire_date.isoformat(),
            'is_hire': self.is_hire,
            'rol': self.rol
            #'user_id': self.user_id
        }

    def from_JSON(self, data):
        for field in ['hire_date', 'is_hire', 'user_id']:
            if field in data:
                setattr(self, field, data[field])'''
