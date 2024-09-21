from app import app
from models import Pet, db

db.drop_all()
db.create_all()

DOG_pic = 'https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_square.jpg'
CAT_pic = 'https://www.humanesociety.org/sites/default/files/styles/400x400/public/2020-10/cat-looking-up-312639.jpg?h=4fe703ed&itok=PbXa-lt7'
BIRD_pic = 'https://statesymbolsusa.org/sites/default/files/primary-images/RobinAmericanRobin.jpg'

dog = Pet(name='Doggo', species='Dog', age='4', notes='This is a good boy', photo_url=DOG_pic)
cat = Pet(name='Kitten', species='Cat', age='3', notes='Little kitten', photo_url=CAT_pic)
bird = Pet(name='Iago', species='Bird', age='9', notes='Wants a cracker', photo_url=BIRD_pic)

db.session.add_all([dog, cat, bird])
db.session.commit()