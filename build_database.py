import os
from config import app,db
from models import Person




PEOPLE = [
    {"fname": "Doug", "lname": "Farrell"},
    {"fname": "Kent", "lname": "Brockman"},
    {"fname": "Bunny", "lname": "Easter"},
    {"fname": "Mohamed", "lname": "Youssef"}
]

if os.path.exists('people.db'):
    os.remove('people.db')

# Create database
db.create_all()

for person in PEOPLE:
    p = Person(lname=person['lname'], fname=person['fname'])
    db.session.add(p)

db.session.commit()
