from ..utils import getConnection
from ..Models import PayPlan
from sqlalchemy.exc import SQLAlchemyError
from app import db

class PayPlanDAO(): 

    @classmethod
    def createPayPlan(self, data):
        try:
            connection = getConnection()
            with connection.cursor() as cursor:
                affectedRows = cursor.rowcount

            nuevoPayPlan = PayPlan(**data)

            db.session.add(nuevoPayPlan)
            db.session.commit()
            connection.close()
            return affectedRows
        except Exception as ex:
            print("error")
            return Exception(ex)
    
    @classmethod
    def getPayPlans(self):
        try:
            allPayPlans = PayPlan.query.all()

            platforms = []
            for platform in allPayPlans:
                platformJson = platform.to_JSON()
                platforms.append(platformJson)
            return platforms
        except Exception as ex:
            print("error")
            raise Exception(ex)

    @classmethod
    def getPayPlanById(self, id):
        try:
            platform = PayPlan.query.filter_by(id=id).first()
            if platform is not None:
                #platformJson = platform.to_JSON()
                return platform
            else:
                return None
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
    
    @classmethod
    def updatePayPlan(self, id, data):
        try:
            platform = PayPlan.query.filter_by(id=id).first()
            if platform is not None:
                platform.from_JSON(data)
                db.session.commit()
                platform_json = platform.to_JSON()
                return platform_json
            else:
                return False
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
        
    @classmethod
    def deletePayPlan(self, id):
        try:
            platform = PayPlan.query.filter_by(id=id).first()
            db.session.delete(platform)
            db.session.commit()
            return platform
        except Exception as ex:
            print("error")
            return Exception(ex)