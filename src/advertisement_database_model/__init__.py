from peewee import *


db = SqliteDatabase('divar_advertisement.db')


class AdvertisementModel(Model):
    title = CharField()
    used_amount = CharField()
    price = CharField()
    location = CharField()
    ad_link = TextField()
    crawled_time = DateField()

    class Meta:
        database = db


db.connect()
db.create_tables([AdvertisementModel])
