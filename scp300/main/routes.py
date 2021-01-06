from scp300.main import bp
from flask import render_template,current_app,request,redirect
from scp300.model.model import Face,Spectacle
from scp300.model import database as db
# from scp300.main.mime import mime 


# index page provide a portal for user to access various function 
# provide brief description for the functionality provided 
@bp.route('/index')
def index():
    return render_template('main/iGAZEhome.html')
    
@bp.route('/search',methods=['GET','POST'])
def search():
    colors = db.session.query(Spectacle.specColor).distinct().all()
    shapes = db.session.query(Spectacle.specShape).distinct().all()
    specs = Spectacle.query.all()
    if request.method == 'POST':
        color= request.form['color']
        shape= request.form['shape']
        previous = { 'color':color , 'shape':shape}
        if color == 'none' and shape == 'none' :
            specs = Spectacle.query.all()
        elif shape=='none':
            specs = Spectacle.query.filter_by(specColor=color).all()
        elif color=='none':
            specs = Spectacle.query.filter_by(specShape=shape).all()
        else:
            specs = Spectacle.query.filter_by(specShape=shape, specColor= color).all()

        return render_template('main/search.html',colors = colors, shapes = shapes, specs = specs , previous = previous )
    return render_template('main/search.html',colors = colors, shapes = shapes, specs = specs)
  

# @mime('text/html')
@bp.route('/fit')
def fit():
    # return render_template('main/threejs_new/examples/300trial.html')
    return redirect("http://localhost/threejs_new/examples/300trial.html")
    # return render_template("scp300/templates/main/threejs_new/examples/300trial.html")
