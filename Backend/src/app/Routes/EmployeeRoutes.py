from ..Models import Employee
from ..Services import EmployeeDAO
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from ..utils import db, loginManagerApp

employeesMain = Blueprint('employeeBlueprint', __name__)

@employeesMain.route('/employees/', methods=['GET', 'POST'])
def handleEmployees():
    try:
        print(request.method)
        if request.method == 'POST':
            data = request.json
            affectedRows = EmployeeDAO.createEmployee(data)
            print(affectedRows)
            if (affectedRows == 0):
                return jsonify({'message': 'Operación POST exitosa'}), 201
            else:
                return jsonify({'message': 'Error on insert'})
        elif request.method == 'GET':
            employees = EmployeeDAO.getEmployees()
            return jsonify(employees), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@employeesMain.route('/employee/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleEmployeeById(id):
    try:
        if request.method == 'GET':
            print(id)
            print("banderaheid1")
            employee = EmployeeDAO.getEmployeeById(id)
            if employee is not None:
                if isinstance(employee, Employee):
                    employeeJSON = employee.to_JSON()
                    return jsonify(employeeJSON), 200
                else:
                    return jsonify({'message': str(ex)}), 500
                
            else:
                return jsonify({'message': 'Employee no encontrado'}), 404
        elif request.method == 'PUT':
            data = request.json
            print(data)
            employee = EmployeeDAO.updateEmployee(id, data)
            if employee is not None:
                return jsonify({'message': 'Employee actualizado con éxito'}), 200
            else:
                return jsonify({'message': 'Employee no encontrado'}), 404
        elif request.method == 'DELETE':
            employee = EmployeeDAO.getEmployeeById(id)
            if employee is not None:
                # Llama a la función que elimina al employee
                is_deleted = EmployeeDAO.deleteEmployee(id)
                if is_deleted:
                    return jsonify({'message': 'Employee eliminado con éxito'}), 200
                else:
                    return jsonify({'message': 'No se pudo eliminar al employee'}), 500
            else:
                return jsonify({'message': 'Employee no encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

@employeesMain.route('/user/employee/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleUserOfEmployeeById(id):
    try:
        if request.method == 'GET':
            employee = EmployeeDAO.getUserEmployee(id)
            if employee is not None:
                return jsonify(employee), 200
            else:
                return jsonify({'message': 'Employee no encontrado'}), 404
        elif request.method == 'PUT':
            return jsonify({'message': 'Employee no encontrado'}), 404
        elif request.method == 'DELETE':
            return jsonify({'message': 'Employee no encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500