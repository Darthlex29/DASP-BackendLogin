from werkzeug.security import check_password_hash, generate_password_hash

class Employee():
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