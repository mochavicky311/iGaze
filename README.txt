

file:   p300.py 
usage:  initialise the flask web server application 

file:   config.py
usage:  contain the configuration to be feed into the server application

folder: main
usage:  main blueprint 
content:index page 

folder: model 
usage:  contain the sql alchemy orm to the database 

folder: recm 
usage: recm blueprint 
content: upload picture, identify face shape, identify 

folder: static 
content: javascript,images/resources, css styling

folder: venv
content: virtual envr of python 

folder: templates
content: html jinja2 templates 

# each blueprint contain an init py file and routes file to route to the corresponding page 

//dependencies :: flask,flask-sqlalchemy,mysql-client 