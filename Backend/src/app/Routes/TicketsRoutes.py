from ..Models import Ticket
from ..Services import TicketDAO
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from ..utils import db, loginManagerApp


ticketsMain = Blueprint('ticketBlueprint', __name__)

@ticketsMain.route('/tickets/', methods=['GET', 'POST'])
def handleTickets():
    try:
        print(request.method)
        if request.method == 'POST':
            data = request.json
            affectedRows = TicketDAO.createTicket(data)
            print(affectedRows)
            if (affectedRows == 0):
                return jsonify({'message': 'Operación POST exitosa'}), 201
            else:
                return jsonify({'message': 'Error on insert'})
        elif request.method == 'GET':
            tickets = TicketDAO.getTickets()
            return jsonify(tickets), 200
        return render_template('auth/create.html')
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@ticketsMain.route('/ticket/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleTicketById(id):
    try:
        if request.method == 'GET':
            ticket = TicketDAO.getTicketById(id)
            if ticket is not None:
                if isinstance(ticket, Ticket):
                    ticketJSON = ticket.to_JSON()
                    return jsonify(ticketJSON), 200
                else:
                    return jsonify({'message': str(ex)}), 500
                
            else:
                return jsonify({'message': 'Ticket no encontrado'}), 404
        elif request.method == 'PUT':
            data = request.json
            print(data)
            ticket = TicketDAO.uptadeTicket(id, data)
            if ticket is not None:
                return jsonify({'message': 'Ticket actualizado con éxito'}), 200
            else:
                return jsonify({'message': 'Ticket no encontrado'}), 404
        elif request.method == 'DELETE':
            ticket = TicketDAO.getTicketById(id)
            if ticket is not None:
                # Llama a la función que elimina al ticket
                is_deleted = TicketDAO.deleteTicket(id)
                if is_deleted:
                    return jsonify({'message': 'Ticket eliminado con éxito'}), 200
                else:
                    return jsonify({'message': 'No se pudo eliminar al ticket'}), 500
            else:
                return jsonify({'message': 'Ticket no encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

