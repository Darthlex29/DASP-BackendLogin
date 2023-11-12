from ..Models import Invoice
from ..utils import getConnection
from app import db

class InvoiceDAO():

    @classmethod
    def createInvoice(self, data):
        try:
            connection = getConnection()
            with connection.cursor() as cursor:
                affectedRows = cursor.rowcount

            nuevoInvoice = Invoice(**data)

            db.session.add(nuevoInvoice)
            db.session.commit()
            connection.close()
            return affectedRows
        except Exception as ex:
            print("error")
            return Exception(ex)
    
    @classmethod
    def getInvoices(self):
        try:
            allInvoices = Invoice.query.all()

            invoices = []
            for invoice in allInvoices:
                invoiceJson = invoice.to_JSON()
                invoices.append(invoiceJson)
            return invoices
        except Exception as ex:
            print("error")
            raise Exception(ex)

    @classmethod
    def getInvoiceById(self, id):
        try:
            invoice = Invoice.query.filter_by(id=id).first()
            if invoice is not None:
                #invoiceJson = invoice.to_JSON()
                return invoice
            else:
                return None
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
    
    @classmethod
    def updateInvoice(self, id, data):
        try:
            invoice = Invoice.query.filter_by(id=id).first()
            if invoice is not None:
                invoice.from_JSON(data)
                db.session.commit()
                invoice_json = invoice.to_JSON()
                return invoice_json
            else:
                return False
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
        
    @classmethod
    def deleteInvoice(self, id):
        try:
            invoice = Invoice.query.filter_by(id=id).first()
            db.session.delete(invoice)
            db.session.commit()
            return invoice
        except Exception as ex:
            print("error")
            return Exception(ex)