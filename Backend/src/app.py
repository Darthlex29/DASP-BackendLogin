from app import createApp, db
from app.Routes.UsersRoutes import userMain
from app.Routes.authRoutes import authMain
from app.Routes.TicketsRoutes import ticketsMain
from app.Routes.EmployeeRoutes import employeesMain
from app.Routes.ClientRoutes import clientsMain
from app.Routes.InvoiceRoutes import invoicesMain
from app.Routes.DistributorRoutes import distributorsMain
from app.Routes.HostingRoutes import hostingsMain


app = createApp('development')

app.register_blueprint(userMain)
app.register_blueprint(authMain)
app.register_blueprint(ticketsMain)
app.register_blueprint(employeesMain)
app.register_blueprint(clientsMain)
app.register_blueprint(invoicesMain)
app.register_blueprint(distributorsMain)
app.register_blueprint(hostingsMain)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run()



