from ..Models import Employee, User
from . import UserDAO
from ..utils import getConnection
from app import db 

class EmployeeDAO():

    @classmethod
    def createEmployee(self, data):
        try:
            connection = getConnection()
            with connection.cursor() as cursor:
                affectedRows = cursor.rowcount

            nuevoEmployee = Employee(**data)

            db.session.add(nuevoEmployee)
            db.session.commit()
            connection.close()
            return affectedRows
        except Exception as ex:
            print("error")
            return Exception(ex)
        
    @classmethod
    def getEmployees(self):
        try:
            allEmployees = Employee.query.all()

            employees = []
            for employee in allEmployees:
                employeeJson = employee.to_JSON()
                employees.append(employeeJson)
            return employees
        except Exception as ex:
            print("error")
            raise Exception(ex)
        
    @classmethod
    def getEmployeeById(self, id):
        try:
            print("bandera1")
            employee = Employee.query.filter_by(id=id).first()
            if employee is not None:
                #employeeJson = employee.to_JSON()
                return employee
            else:
                return None
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
    
    @classmethod
    def updateEmployee(self, id, data):
        try:
            employee = Employee.query.filter_by(id=id).first()
            if employee is not None:
                employee.from_JSON(data)
                db.session.commit()
                employee_json = employee.to_JSON()
                return employee_json
            else:
                return False
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
        
    @classmethod
    def deleteEmployee(self, id):
        try:
            employee = Employee.query.filter_by(id=id).first()
            db.session.delete(employee)
            db.session.commit()
            return employee
        except Exception as ex:
            print("error")
            return Exception(ex)
        
    @classmethod
    def getUserEmployee(self, id):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT Employee.*, User.* FROM Employee JOIN User ON Employee.user_id = User.id WHERE Employee.id = %s", (id,))
                result = cursor.fetchone()
                print(result)
            if result:
                if hasattr(result, '__iter__'):
                    user = User(
                        name=result[5],
                        email=result[6],
                        password=result[7],
                        idDocument=result[8],
                        documentType=result[9]
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
            
