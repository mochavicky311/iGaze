from scp300.main import bp as main_bp 
from scp300.recm import bp as recm_bp
from flask import Flask 
from config import Config
from scp300.model import database as db
from scp300.recm.predict import model
from flask_mime import Mime
# from scp300.main.mime import mime



# factory function to create python flask server dynamically 
def create_app():
    # create flask object 
    application = Flask(__name__)
    application.config.from_object(Config)
    db.init_app(application)
    # mime.init_app(application)
    application.register_blueprint(main_bp,url_prefix="/main")
    application.register_blueprint(recm_bp,url_prefix="/recm")

    return application
    

