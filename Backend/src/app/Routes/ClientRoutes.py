from ..Models import Client
from ..Services import ClientDAO
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from ..utils import db, loginManagerApp

clientsMain = Blueprint('clientBlueprint', __name__)

@clientsMain.route('/clients/', methods=['GET', 'POST'])
def handleClients():
    try:
        print(request.method)
        if request.method == 'POST':
            data = request.json
            affectedRows = ClientDAO.createClient(data)
            print(affectedRows)
            if (affectedRows == 0):
                return jsonify({'message': 'Operación POST exitosa'}), 201
            else:
                return jsonify({'message': 'Error on insert'})
        elif request.method == 'GET':
            clients = ClientDAO.getClients()
            return jsonify(clients), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@clientsMain.route('/client/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleClientById(id):
    try:
        if request.method == 'GET':
            print(id)
            print("banderaheid1")
            client = ClientDAO.getClientById(id)
            if client is not None:
                if isinstance(client, Client):
                    clientJSON = client.to_JSON()
                    return jsonify(clientJSON), 200
                else:
                    return jsonify({'message': str(ex)}), 500
                
            else:
                return jsonify({'message': 'Client no encontrado'}), 404
        elif request.method == 'PUT':
            data = request.json
            print(data)
            client = ClientDAO.updateClient(id, data)
            if client is not None:
                return jsonify({'message': 'Client actualizado con éxito'}), 200
            else:
                return jsonify({'message': 'Client no encontrado'}), 404
        elif request.method == 'DELETE':
            client = ClientDAO.getClientById(id)
            if client is not None:
                # Llama a la función que elimina al client
                is_deleted = ClientDAO.deleteClient(id)
                if is_deleted:
                    return jsonify({'message': 'Client eliminado con éxito'}), 200
                else:
                    return jsonify({'message': 'No se pudo eliminar al client'}), 500
            else:
                return jsonify({'message': 'Client no encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

@clientsMain.route('/user/client/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleUserOfClientById(id):
    try:
        if request.method == 'GET':
            client = ClientDAO.getUserClient(id)
            if client is not None:
                return jsonify(client), 200
            else:
                return jsonify({'message': 'Client no encontrado'}), 404
        elif request.method == 'PUT':
            return jsonify({'message': 'Client no encontrado'}), 404
        elif request.method == 'DELETE':
            return jsonify({'message': 'Client no encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500