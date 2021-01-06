from flask import Blueprint


#blueprint initialization 
bp = Blueprint('main',__name__)
from scp300.main import routes
