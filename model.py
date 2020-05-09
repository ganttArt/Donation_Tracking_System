import os
from peewee import Model, CharField, IntegerField, ForeignKeyField, DateTimeField
from playhouse.db_url import connect
from datetime import datetime

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class Donor(Model):
    name = CharField(max_length=255, unique=True)
    email = CharField(max_length=100, null=True, unique=True)
    date_added = DateTimeField(default=datetime.now)

    class Meta:
        database = db

class Donation(Model):
    value = IntegerField()
    donor = ForeignKeyField(Donor, backref='donations')
    date = DateTimeField(default=datetime.now)

    class Meta:
        database = db

