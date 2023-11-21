from flask_login import current_user
from ..Models import Buyout, Domain, Hosting

class Verifications():
    
    @classmethod
    def VerificationBuyoutOfCurrentUser(self):
        # Obtener el ID del usuario loggeado
        user_id = current_user.id if current_user.is_authenticated else None
        # Verificar si el usuario tiene un Buyout en estado 'Pending'
        if user_id is not None:
            existing_pending_buyout = Buyout.query.filter_by(user_id=user_id, status='Pending').first()
            if not existing_pending_buyout:
                return None
            else: 
                return existing_pending_buyout.id  
        else: 
            return {'error': 'No se encontró un usuario loggeado.'}, 401
        
    @classmethod
    def getBuyoutsOfCurrentUser(self):
        # Obtener el ID del usuario loggeado
        user_id = current_user.id if current_user.is_authenticated else None
        # Obtener los Buyouts asociados al usuario actual
        if user_id is not None:
            user_buyouts = Buyout.query.filter_by(user_id=user_id).all()
            #return [buyout.to_JSON() for buyout in user_buyouts]
            return user_buyouts
        else:
            return None

        
    @classmethod
    def getDomainsOfCurrentUser(self):
        # Obtener el ID del usuario loggeado
        user_id = current_user.id if current_user.is_authenticated else None
        # Obtener los Dominios asociados al usuario actual
        if user_id is not None:
            user_domains = Domain.query.join(Buyout).filter(Buyout.user_id == user_id).all()
            #return [domain.to_JSON() for domain in user_domains]
            return user_domains
        else:
            return None
        
    @classmethod
    def getHostingsOfCurrentUser(self):
        # Obtener el ID del usuario loggeado
        user_id = current_user.id if current_user.is_authenticated else None
        # Obtener los Hostings asociados al usuario actual
        if user_id is not None:
            user_hostings = Hosting.query.join(Buyout).filter(Buyout.user_id == user_id).all()
            #return [hosting.to_JSON() for hosting in user_hostings]
            return user_hostings
        else:
            return None
