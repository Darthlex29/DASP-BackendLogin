from ..Models import Distributor
from ..Services import DistributorDAO
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from ..utils import db, loginManagerApp


distributorsMain = Blueprint('distributorBlueprint', __name__)

@distributorsMain.route('/distributors/', methods=['GET', 'POST'])
def handleDistributors():
    try:
        print(request.method)
        if request.method == 'POST':
            data = request.json
            affectedRows = DistributorDAO.createDistributor(data)
            print(affectedRows)
            if (affectedRows == 0):
                return jsonify({'message': 'Operación POST exitosa'}), 201
            else:
                return jsonify({'message': 'Error on insert'})
        elif request.method == 'GET':
            distributors = DistributorDAO.getDistributors()
            return jsonify(distributors), 200
        return render_template('auth/create.html')
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@distributorsMain.route('/distributor/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleDistributorById(id):
    try:
        if request.method == 'GET':
            distributor = DistributorDAO.getDistributorByID(id)
            if distributor is not None:
                if isinstance(distributor, Distributor):
                    distributorJSON = distributor.to_JSON()
                    return jsonify(distributorJSON), 200
                else:
                    return jsonify({'message': str(ex)}), 500
                
            else:
                return jsonify({'message': 'Distributor no encontrado'}), 404
        elif request.method == 'PUT':
            data = request.json
            print(data)
            distributor = DistributorDAO.uptadeDistributor(id, data)
            if distributor is not None:
                return jsonify({'message': 'Distributor actualizado con éxito'}), 200
            else:
                return jsonify({'message': 'Distributor no encontrado'}), 404
        elif request.method == 'DELETE':
            distributor = DistributorDAO.getDistributorByID(id)
            if distributor is not None:
                # Llama a la función que elimina al distributor
                is_deleted = DistributorDAO.deleteDistributor(id)
                if is_deleted:
                    return jsonify({'message': 'Distributor eliminado con éxito'}), 200
                else:
                    return jsonify({'message': 'No se pudo eliminar al distributor'}), 500
            else:
                return jsonify({'message': 'Distributor no encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

