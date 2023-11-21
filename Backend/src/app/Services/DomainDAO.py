from ..Models import Domain
from .Verifications import Verifications
from ..utils import getConnection
from app import db

class DomainDAO():

    @classmethod
    def createDomain(self, data):
        try:
        
            connection = getConnection()
            with connection.cursor() as cursor:
                affectedRows = cursor.rowcount

            # Verificar el Buyout pendiente del usuario actual
            verification_result = Verifications.VerificationBuyoutOfCurrentUser()
            print("Despues de la verificacion: ")
            print(verification_result)

            nuevoDomain = Domain(**data)
            if verification_result is not None: 
                if 'error' in verification_result:
                    return verification_result
                else:
                    nuevoDomain.buyout_id = verification_result     
            
             # Agregar y confirmar cambios en la sesión de SQLAlchemy
            #db.session.add(nuevoDomain)
            #db.session.commit()
            #connection.close()
            return affectedRows
        except Exception as ex:
            print("error")
            return Exception(ex)
    
    @classmethod
    def getDomains(self):
        try:
            allDomains = Domain.query.all()
            return allDomains
        except Exception as ex:
            print("error")
            raise Exception(ex)

    @classmethod
    def getDomainById(self, id):
        try:
            domain = Domain.query.filter_by(id=id).first()
            if domain is not None:
                #domainJson = domain.to_JSON()
                return domain
            else:
                return None
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
    
    @classmethod
    def updateDomain(self, id, data):
        try:
            domain = Domain.query.filter_by(id=id).first()
            if domain is not None:
                domain.from_JSON(data)
                db.session.commit()
                domain_json = domain.to_JSON()
                return domain_json
            else:
                return False
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
        
    @classmethod
    def deleteDomain(self, id):
        try:
            domain = Domain.query.filter_by(id=id).first()
            db.session.delete(domain)
            db.session.commit()
            return domain
        except Exception as ex:
            print("error")
            return Exception(ex)
        
    @classmethod
    def getDomainsDistributors(self, domain):
        return domain.distributors