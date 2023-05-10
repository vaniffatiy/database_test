from peewee import *

conn = SqliteDatabase('Chinook_Sqlite.sqlite')


class BaseModel(Model):
    class Meta:
        database = conn


class Artist(BaseModel):
    artist_id = AutoField(column_name='ArtistId')
    name = TextField(column_name='Name', null=True)

    class Meta:
        table_name = 'Artist'


def print_last_five_artists():
    print('########################################################')
    cur_query = Artist.select().limit(5).order_by(Artist.artist_id.desc())
    for item in cur_query.dicts().execute():
        print('artist: ', item)
