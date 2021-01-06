from scp300.model import database as db 


# setup database table and relationship here 
# relationship refer flask-sqlalchemy tutorial 
class Face(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    specColor = db.Column(db.String(10),nullable=False)
    specShape = db.Column(db.String(10),nullable=False)
    imageURL = db.Column(db.String(50),nullable=False)
    faceShape = db.Column(db.String(10),nullable=False)

    def __repr__(self):
        return '{"id":%d ,"specColor":"%s", "specShape":"%s", "imageURL":"%s"}' % (self.id,self.specColor,self.specColor,self.imageURL)

class Spectacle(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    specName = db.Column(db.String(50),nullable=False)
    specColor = db.Column(db.String(10),nullable=False)
    specShape = db.Column(db.String(10),nullable=False)
    imageURL = db.Column(db.String(50),nullable=False)
    shoppingURL = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return 'id:%d,specName:%s,specColor:%s,specShape:%s,imageURL:%s,shoppingURL:%s' % (self.id,self.specName,self.specColor,self.specShape,self.imageURL,self.shoppingURL)

    
    
