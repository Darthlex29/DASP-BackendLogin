from decouple import config
import pytz
import datetime
import jwt

class Security():

    secret = config('JWT_KEY')
    tz = pytz.timezone("America/Bogota")

    @classmethod
    def generateToken(cls, authenticated_user):
        payload = {
            'iat':datetime.datetime.now(tz=cls.tz),
            'exp':datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=100),
            'email': authenticated_user.email,
            'name': authenticated_user.name
        }
        return jwt.encode(payload, cls.secret, algorithm = "HS256")


    @classmethod 
    def verifyToken(cls, headers):
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']
            encodedToken = authorization.split(" ")[1]

            try: 
                payload=jwt.decode(encodedToken, cls.secret, algorithms = ["HS256"])
                return True
            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                print("error")
                return False
        print("no entra en el if")
        return False