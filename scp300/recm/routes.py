from scp300.recm import bp
from flask import render_template,request,flash,redirect,url_for
from flask import current_app
from werkzeug.utils import secure_filename
from scp300.model.model import Face,Spectacle
from scp300.recm.predict import model,predict_face_shape
from random import * 

import os


@bp.route('/snapshot',methods=["GET","POST"])
def snap():
    if request.method == "POST":
        f = request.files['image']
        if( f ):
            current_app.logger.info('image exist')
            current_app.logger.info(f.filename)
            #f.save(os.path.join(current_app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            location = os.path.join(current_app.config['UPLOAD_FOLDER'],secure_filename(f.filename))
            f.save(location)
            #f.save(secure_filename(f.filename))
            flash("the face is up loaded succesfully") 
            return  url_for('recm.result')
        else:
            current_app.logger.info('image doesnt exist')     
    return render_template('recm/snapshot.html')

@bp.route('/result')
def result():
    # the return result of the query is actualy object which need to be accessed using Object.attribute else the output will be weird 
    # however sqlalchemy flask is rather confusing in the way if require more implementation might need more specifci tutorial on flask sqlalchemy 
    # sql alchemy
    shape = predict_face_shape()
    current_app.logger.info(shape)
    #shape= "heart"
    # stub variable before integrating face recognizer variable 
    face = Face.query.filter_by(faceShape=shape)
    rdnum = randint(1,500)
    return render_template('recm/result.html',shape=shape,faces=face, rand=rdnum)
    
