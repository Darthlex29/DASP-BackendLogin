from ..Models import Invoice
from ..Services import InvoiceDAO
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from ..utils import db, loginManagerApp


invoicesMain = Blueprint('invoiceBlueprint', __name__)

@invoicesMain.route('/invoices/', methods=['GET', 'POST'])
def handleInvoices():
    try:
        print(request.method)
        if request.method == 'POST':
            data = request.json
            affectedRows = InvoiceDAO.createInvoice(data)
            print(affectedRows)
            if (affectedRows == 0):
                return jsonify({'message': 'Operación POST exitosa'}), 201
            else:
                return jsonify({'message': 'Error on insert'})
        elif request.method == 'GET':
            invoices = InvoiceDAO.getInvoices()
            return jsonify(invoices), 200
        return render_template('auth/create.html')
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@invoicesMain.route('/invoice/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleInvoiceById(id):
    try:
        if request.method == 'GET':
            invoice = InvoiceDAO.getInvoiceById(id)
            if invoice is not None:
                if isinstance(invoice, Invoice):
                    invoiceJSON = invoice.to_JSON()
                    return jsonify(invoiceJSON), 200
                else:
                    return jsonify({'message': str(ex)}), 500
                
            else:
                return jsonify({'message': 'Invoice no encontrado'}), 404
        elif request.method == 'PUT':
            data = request.json
            print(data)
            invoice = InvoiceDAO.updateInvoice(id, data)
            if invoice is not None:
                return jsonify({'message': 'Invoice actualizado con éxito'}), 200
            else:
                return jsonify({'message': 'Invoice no encontrado'}), 404
        elif request.method == 'DELETE':
            invoice = InvoiceDAO.getInvoiceById(id)
            if invoice is not None:
                # Llama a la función que elimina al invoice
                is_deleted = InvoiceDAO.deleteInvoice(id)
                if is_deleted:
                    return jsonify({'message': 'Invoice eliminado con éxito'}), 200
                else:
                    return jsonify({'message': 'No se pudo eliminar al invoice'}), 500
            else:
                return jsonify({'message': 'Invoice no encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

