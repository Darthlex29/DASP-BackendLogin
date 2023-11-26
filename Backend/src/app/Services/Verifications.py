from flask_login import current_user
from ..Models import Buyout, Domain, Hosting
from .BuyoutDAO import BuyoutDAO
from app import db

class Verifications():
    
    @classmethod
    def VerificationBuyoutOfCurrentUser(self, idUser):
        # Obtener el ID del usuario loggeado
        try: 
            user_id = current_user.id if current_user.is_authenticated else idUser
            # Verificar si el usuario tiene un Buyout en estado 'Pending'

            if user_id is not None:
                existing_pending_buyout = Buyout.query.filter_by(user_id=user_id, status='Pending').first()
                if not existing_pending_buyout:
                    print('el usuario no tiene buyout')
                    data = self.createPendingBuyout(user_id)
                    nuevoBuyout = Buyout(**data)
                    db.session.add(nuevoBuyout)
                    db.session.commit()
                    return nuevoBuyout.id
                else: 
                    print('Si hay un buyout')
                    return existing_pending_buyout.id  
            else: 
                print("No hay usuario loggeado")
                return None
        except Exception as ex:
            print("error")
            return Exception(ex)
        
    @classmethod
    def createPendingBuyout(cls, user_id):
        return Buyout(pay_plan_id=1, status="Pending", user_id=user_id)
        
    @classmethod
    def getItemsOfUser(cls, user_model, user_id=None):
        user_id = current_user.id if current_user.is_authenticated else user_id
        if user_id is not None:
            return user_model.query.join(Buyout).filter(Buyout.user_id == user_id).all()
        else:
            return None

    @classmethod
    def getDomainsOfCurrentUser(cls, user_id=None):
        return cls.getItemsOfUser(Domain, user_id)

    @classmethod
    def getHostingsOfCurrentUser(cls, user_id=None):
        return cls.getItemsOfUser(Hosting, user_id)
    
    @classmethod
    def getBuyoutsOfCurrentUser(self, idUser=None):
        user_id = current_user.id if current_user.is_authenticated else idUser
        if user_id is not None:
            user_buyouts = Buyout.query.filter_by(user_id=user_id).all()
            #return [buyout.to_JSON() for buyout in user_buyouts]
            return user_buyouts
        else:
            return None

    '''
    @classmethod
    def getBuyoutsOfCurrentUser(self, idUser=None):
        # Obtener el ID del usuario loggeado o utilizar el ID proporcionado
        user_id = current_user.id if current_user.is_authenticated else idUser
        # Obtener los Buyouts asociados al usuario actual
        if user_id is not None:
            user_buyouts = Buyout.query.filter_by(user_id=user_id).all()
            #return [buyout.to_JSON() for buyout in user_buyouts]
            return user_buyouts
        else:
            return None

        
    @classmethod
    def getDomainsOfCurrentUser(cls, idUser=None):
        # Obtener el ID del usuario loggeado o utilizar el ID proporcionado
        user_id = current_user.id if current_user.is_authenticated else idUser
        # Obtener los Dominios asociados al usuario actual
        if user_id is not None:
            user_domains = Domain.query.join(Buyout).filter(Buyout.user_id == user_id).all()
            return user_domains
        else:
            return None
        
    @classmethod
    def getHostingsOfCurrentUser(self, idUser=None):
        # Obtener el ID del usuario loggeado
        user_id = current_user.id if current_user.is_authenticated else idUser
        # Obtener los Hostings asociados al usuario actual
        if user_id is not None:
            user_hostings = Hosting.query.join(Buyout).filter(Buyout.user_id == user_id).all()
            return user_hostings
        else:
            return None
    '''
    
