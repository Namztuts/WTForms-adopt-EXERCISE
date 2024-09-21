from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
    
class Pet(db.Model):
    '''Pet model'''
    
    __tablename__ = 'pets'
    
    def __repr__(self):
        pet=self
        return f"<Pet name= {pet.name} | species= {pet.species} | age= {pet.age} | available= {pet.available} | notes= {pet.notes} | photo_url= {pet.photo_url}"
  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    available = db.Column(db.Boolean, nullable=False, default=True)
    notes = db.Column(db.Text)
    photo_url = db.Column(db.Text) # not sure why the default pic is not working | default True is working
    