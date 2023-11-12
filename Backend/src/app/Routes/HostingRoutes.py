from ..Models import Hosting
from ..Services import HostingDAO
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from ..utils import db, loginManagerApp


hostingsMain = Blueprint('hostingBlueprint', __name__)

@hostingsMain.route('/hostings/', methods=['GET', 'POST'])
def handleHostings():
    try:
        print(request.method)
        if request.method == 'POST':
            data = request.json
            affectedRows = HostingDAO.createHosting(data)
            print(affectedRows)
            if (affectedRows == 0):
                return jsonify({'message': 'Operación POST exitosa'}), 201
            else:
                return jsonify({'message': 'Error on insert'})
        elif request.method == 'GET':
            hostings = HostingDAO.getHostings()
            return jsonify(hostings), 200
        return render_template('auth/create.html')
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@hostingsMain.route('/hosting/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleHostingById(id):
    try:
        if request.method == 'GET':
            hosting = HostingDAO.getHostingById(id)
            if hosting is not None:
                if isinstance(hosting, Hosting):
                    hostingJSON = hosting.to_JSON()
                    return jsonify(hostingJSON), 200
                else:
                    return jsonify({'message': str(ex)}), 500
                
            else:
                return jsonify({'message': 'Hosting no encontrado'}), 404
        elif request.method == 'PUT':
            data = request.json
            print(data)
            hosting = HostingDAO.updateHosting(id, data)
            if hosting is not None:
                return jsonify({'message': 'Hosting actualizado con éxito'}), 200
            else:
                return jsonify({'message': 'Hosting no encontrado'}), 404
        elif request.method == 'DELETE':
            hosting = HostingDAO.getHostingById(id)
            if hosting is not None:
                # Llama a la función que elimina al hosting
                is_deleted = HostingDAO.deleteHosting(id)
                if is_deleted:
                    return jsonify({'message': 'Hosting eliminado con éxito'}), 200
                else:
                    return jsonify({'message': 'No se pudo eliminar al hosting'}), 500
            else:
                return jsonify({'message': 'Hosting no encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

