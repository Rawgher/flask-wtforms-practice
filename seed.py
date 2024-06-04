"""Seed file to make sample data for the pets db."""

from models import Pet, db
from app import app

# Push the application context
with app.app_context():
    
    # Create all tables
    db.drop_all()
    db.create_all()

    # If table isn't empty, empty it
    Pet.query.delete()

    # Add pets
    pet1 = Pet(name='Comet', species='dog', photo_url='https://images.unsplash.com/photo-1518717758536-85ae29035b6d?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', age=5)
    pet2 = Pet(name='Shadow', species='dog', photo_url='https://images.unsplash.com/photo-1561037404-61cd46aa615b?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', age=2)
    pet3 = Pet(name='Chip', species='cat', photo_url='https://images.unsplash.com/photo-1583795128727-6ec3642408f8?q=80&w=2714&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', age=1)
    pet4 = Pet(name='Lumpy', species='cat', age=5, notes='not friendly', available=False)
    pet5 = Pet(name='Ragnar', species='cat', photo_url='https://images.unsplash.com/photo-1589883661923-6476cb0ae9f2?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', age=5)
    pet6 = Pet(name='Spike', species='porcupine', age=3, notes='he has a prickly personality', available=False)

    # Add new objects to session, so they'll persist
    db.session.add_all([pet1, pet2, pet3, pet4, pet5, pet6])

    # Commit--otherwise, this never gets saved!
    db.session.commit()