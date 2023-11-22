from ..Models import Country
from ..Services import CountryDAO, Calculator
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from ..utils import db, loginManagerApp
from ..utils import Security


countriesMain = Blueprint('countryBlueprint', __name__)

@countriesMain.route('/countries/', methods=['GET', 'POST'])
def handleCountries():
        try:
            print(request.method)
            if request.method == 'POST':
                hasAccess = Security.verifyToken(request.headers, required_role=3)
                if hasAccess:
                    data = request.json
                    affectedRows = CountryDAO.createCountry(data)
                    print(affectedRows)
                    if (affectedRows == 0):
                        return jsonify({'message': 'Operación POST exitosa'}), 201
                    else:
                        return jsonify({'message': 'Error on insert'})
                else: 
                    return jsonify({'message': 'Unauthorized'}), 401
            elif request.method == 'GET':
                hasAccess=Security.verifyToken(request.headers)
                if hasAccess:
                    countries = CountryDAO.getCountries()
                    return jsonify(countries), 200
                else: 
                    return jsonify({'message': 'Unauthorized'}), 401
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500


@countriesMain.route('/country/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleCountryById(id):
    hasAccess=Security.verifyToken(request.headers)
    if hasAccess:
        try:
            if request.method == 'GET':
                country = CountryDAO.getCountryById(id)

                if country is not None:
                    if isinstance(country, Country):
                        countryJSON = country.to_JSON()
                        return jsonify(countryJSON), 200
                    else:
                        return jsonify({'message': str(ex)}), 500
                    
                else:
                    return jsonify({'message': 'Country no encontrado'}), 404
            elif request.method == 'PUT':
                hasAccess = Security.verifyToken(request.headers, required_role=3)
                if hasAccess:
                    data = request.json
                    print(data)
                    country = CountryDAO.getCountryById(id, data)
                    if country is not None:
                        return jsonify({'message': 'Country actualizado con éxito'}), 200
                    else:
                        return jsonify({'message': 'Country no encontrado'}), 404
                else: 
                    return jsonify({'message': 'Unauthorized'}), 401
            elif request.method == 'DELETE':
                hasAccess = Security.verifyToken(request.headers, required_role=3)
                if hasAccess:
                    country = CountryDAO.getCountryById(id)
                    if country is not None:
                        # Llama a la función que elimina al country
                        is_deleted = CountryDAO.deleteCountry(id)
                        if is_deleted:
                            return jsonify({'message': 'Country eliminado con éxito'}), 200
                        else:
                            return jsonify({'message': 'No se pudo eliminar al country'}), 500
                    else:
                        return jsonify({'message': 'Country no encontrado'}), 404
                else: 
                    return jsonify({'message': 'Unauthorized'}), 401
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    else: 
        return jsonify({'message': 'Unauthorized'}), 401