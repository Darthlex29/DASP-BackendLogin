from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from ..Models import User, UserVO
from ..Services import UserDAO

userMain = Blueprint('userBlueprint', __name__)

@userMain.route('/')
def index():
    return "Hello, Mr. Sun! La tierra les dice hola"

@userMain.route('/users/', methods=['GET', 'POST'])
def handleUsers():
    try:
        print(request.method)
        if request.method == 'POST':
            data = request.json
            print('bandera1')
            print(data)
            affectedRows = UserDAO.createUser(data)
            print(affectedRows)
            if (affectedRows == 0):
                return jsonify({'message': 'Operación POST exitosa'}), 201
            else:
                return jsonify({'message': 'Error on insert'})
        elif request.method == 'GET':
            users = UserDAO.getUsers()
            return jsonify(users), 200
        return render_template('auth/create.html')
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@userMain.route('/user/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleUserById(id):
    try:
        if request.method == 'GET':
            user = UserDAO.getUserByID(id)
            if user is not None:
                if isinstance(user, User):
                    userJSON = user.to_JSON()
                    return jsonify(userJSON), 200
                else:
                    return jsonify({'message': str(ex)}), 500
                
            else:
                return jsonify({'message': 'Usuario no encontrado'}), 404
        elif request.method == 'PUT':
            data = request.json
            print(data)
            user = UserDAO.uptadeUser(id, data)
            if user is not None:
                return jsonify({'message': 'Usuario actualizado con éxito'}), 200
            else:
                return jsonify({'message': 'Usuario no encontrado'}), 404
        elif request.method == 'DELETE':
            user = UserDAO.getUserByID(id)
            if user is not None:
                # Llama a la función que elimina al usuario
                is_deleted = UserDAO.deleteUser(id)
                if is_deleted:
                    return jsonify({'message': 'Usuario eliminado con éxito'}), 200
                else:
                    return jsonify({'message': 'No se pudo eliminar al usuario'}), 500
            else:
                return jsonify({'message': 'Usuario no encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@userMain.route('/user/<string:email>', methods=['GET', 'PUT', 'DELETE'])
def handleUserByEmail(email):
    try:
        if request.method == 'GET':
            user = UserDAO.getUserByEmail(email)
            if user is not None:
                return jsonify(user), 200
            else:
                return jsonify({'message': 'Usuario no encontrado'}), 404
        elif request.method == 'PUT':
            return jsonify({'message': 'Funcion no habilitada'}), 501
        elif request.method == 'DELETE':
            return jsonify({'message': 'Funcion no habilitada'}), 501

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# Eliminar los que esten de aqui para abajo 

@userMain.route('/test/', methods=['GET', 'POST'])
def testing():
    try:
        print(request.method)
        if request.method == 'POST':
            data = request.json
            UserDAO.createUserHP(data)
            return jsonify({''}), 200
        elif request.method == 'GET':
            users = UserDAO.getUsers()
            return jsonify(users), 200
        return render_template('auth/create.html')
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@userMain.route('/users/sinhp/', methods=['GET', 'POST'])
def create():
    try:
        print(request.method)
        if request.method == 'POST':
            data = request.json
            affectedRows = UserDAO.create_User(data)
            if affectedRows == 0:
                return jsonify({'message': 'Operación POST exitosa'}), 201
            else:
                return jsonify({'message': 'Error on insert'})
        elif request.method == 'GET':
            users = UserDAO.getUsers()
            return jsonify(users), 200
        return render_template('auth/create.html')
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500