from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

app.app_context().push()
connect_db(app)

DEFAULT_pic = 'https://media.istockphoto.com/id/931785704/vector/paw_print.jpg?s=612x612&w=0&k=20&c=CXBPHlf7XHdJiiOULJrI9nGZjVNAj7cqnkM_eDyDdCU='
#use the above as the default photo_url | if nothing is input in the form than the value is "null" and never actually empty so you can't use default in the model

@app.route("/")
def homepage():
    """Show homepage with pets"""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    '''Add new snack'''
    form = PetForm()
    
    if form.validate_on_submit():
        name = form.name.data   
        species = form.species.data
        age = form.age.data
        notes = form.notes.data
        photo_url = form.photo_url.data or DEFAULT_pic
        flash(f"{name} the {species} has been added!")
        
        pet = Pet(name=name, species=species, age=age, notes=notes, photo_url=photo_url)
        db.session.add(pet)
        db.session.commit()
        
        return redirect('/')
        
    else:
        return render_template('add_pet.html', form=form)
    
@app.route('/<int:pet_id>', methods=["GET", "POST"])
def pet_info(pet_id):
    '''Shows info about a specific pet'''
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data or DEFAULT_pic
        
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template('pet_details.html', pet=pet, form=form)