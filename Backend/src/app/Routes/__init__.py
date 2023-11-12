from flask import Blueprint

# Crea una instancia de Blueprint llamada "bp"
bp = Blueprint('mainBlueprint', __name__)

# Importa las rutas que deseas asociar con "bp"
from . import authRoutes
from . import UsersRoutes
from . import TicketsRoutes
from . import EmployeeRoutes
from . import ClientRoutes
from . import DistributorRoutes
from . import HostingRoutes
from . import InvoiceRoutes

# Agrega las rutas al Blueprint

mainRoute = bp