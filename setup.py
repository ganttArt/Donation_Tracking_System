import random

from model import db, Donor, Donation 

db.connect()

# This line will allow you "upgrade" an existing database by
# dropping all existing tables from it.
# db.drop_tables([Donor, Donation])

db.create_tables([Donor, Donation])

alice = Donor(name="Alice Stephenson", email="stepali@gmail.com")
alice.save()

bob = Donor(name="Bob Novak", email='bnovak@gmail.com')
bob.save()

charlie = Donor(name="Charlie Harper", email='harpster@gmail.com')
charlie.save()

donors = [alice, bob, charlie]

for donor in donors:
    Donation(donor=donor, value=random.randint(100, 10000)).save()

