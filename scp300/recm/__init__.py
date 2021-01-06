from flask import Blueprint
# Blueprint initialisation
bp = Blueprint('recm',__name__) 

from scp300.recm import routes