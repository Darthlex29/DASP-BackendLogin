from decouple import config
import pytz
import datetime
import jwt
from sqlalchemy import true

class Security():

    secret = config('JWT_KEY')
    tz = pytz.timezone("America/Bogota")

    @classmethod
    def generateToken(cls, authenticated_user):
        print("Rol del usuario autenticado: ")
        print(authenticated_user.rol_id)
        payload = {
            'iat':datetime.datetime.now(tz=cls.tz),
            'exp':datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=100),
            'email': authenticated_user.email,
            'name': authenticated_user.name,
            'rol_id':authenticated_user.rol_id
        }
        return jwt.encode(payload, cls.secret, algorithm = "HS256")


    @classmethod
    def verifyToken(cls, headers, required_role=None):
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']
            encodedToken = authorization.split(" ")[1]
            try:
                payload = jwt.decode(encodedToken, cls.secret, algorithms=["HS256"])
                user_role = payload.get('rol_id')
                
                if required_role is not None and (user_role != 3 and user_role != required_role):
                    print(f"Usuario no autorizado para realizar esta acción. Se requiere el rol: {required_role}")
                    return False

                return True

            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                print("Error 009: Token inválido o expirado.")
                return False
        return False