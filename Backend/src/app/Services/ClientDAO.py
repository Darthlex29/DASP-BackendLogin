from ..Models import Client, User
from . import UserDAO
from ..utils import getConnection
from app import db 

class ClientDAO():

    @classmethod
    def createClient(self, data):
        try:
            connection = getConnection()
            with connection.cursor() as cursor:
                affectedRows = cursor.rowcount

            nuevoClient = Client(**data)

            db.session.add(nuevoClient)
            db.session.commit()
            connection.close()
            return affectedRows
        except Exception as ex:
            print("error")
            return Exception(ex)
        
    @classmethod
    def getClients(self):
        try:
            allClients = Client.query.all()

            clients = []
            for client in allClients:
                clientJson = client.to_JSON()
                clients.append(clientJson)
            return clients
        except Exception as ex:
            print("error")
            raise Exception(ex)
        
    @classmethod
    def getClientById(self, id):
        try:
            client = Client.query.filter_by(id=id).first()
            if client is not None:
                #clientJson = client.to_JSON()
                return client
            else:
                return None
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
    
    @classmethod
    def updateClient(self, id, data):
        try:
            client = Client.query.filter_by(id=id).first()
            if client is not None:
                client.from_JSON(data)
                db.session.commit()
                client_json = client.to_JSON()
                return client_json
            else:
                return False
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
        
    @classmethod
    def deleteClient(self, id):
        try:
            client = Client.query.filter_by(id=id).first()
            db.session.delete(client)
            db.session.commit()
            return client
        except Exception as ex:
            print("error")
            return Exception(ex)
        
    @classmethod
    def getUserClient(self, id):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT Client.*, User.* FROM Client JOIN User ON Client.user_id = User.id WHERE Client.id = %s", (id,))
                result = cursor.fetchone()
                print(result)
            if result:
                if hasattr(result, '__iter__'):
                    user = User(
                        name=result[8],
                        email=result[9],
                        password=result[10],
                        idDocument=result[11],
                        documentType=result[12]
                    )
                    user.id=result[4]
                    userJson = user.to_JSON()
                    print(userJson)
                    connection.close()
                    return userJson
                else:
                    print("Resultado no iterable:", result)
            else:
                return None
        except Exception as ex:
            print("Error 404:", ex)
            return Exception(ex)
            