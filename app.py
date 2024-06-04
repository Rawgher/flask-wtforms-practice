from flask import Flask, redirect, render_template
from models import db, connect_db, Pet
from forms import PetForm
from flask_debugtoolbar import DebugToolbarExtension
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "secretkey"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Route for adding a pet and displaying the form"""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template(
            "add-pet.html", form=form)
    
@app.route("/pet/<int:pet_id>")
def get_pet(pet_id):
    """Route for viewing an individual pet"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet.html', pet=pet)

@app.route("/pet/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Route for editing a pet and displaying the form"""
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect(f"/pet/{pet_id}")

    else:
        return render_template(
            "edit-pet.html", form=form)