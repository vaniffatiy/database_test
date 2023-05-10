from models import *


cursor = conn.cursor()
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")


results = cursor.fetchall()
print(results)


artist = Artist.get(Artist.artist_id == 1)
print('artist: ', artist.artist_id, artist.name)


query = Artist.select()
print(query)


query = Artist.select().where(Artist.artist_id < 10).\
                        limit(5).order_by(Artist.artist_id.desc())
print(query)


artists_selected = query.dicts().execute()
print(artists_selected)


for artist in artists_selected:
    print('artist: ', artist)


Artist.create(name='1-Qwerty')


artist = Artist(name='2-asdfg')
artist.save()


artists_data = [{'name': '3-qaswed'}, {'name': '4-yhnbgt'}]
Artist.insert_many(artists_data).execute()
print_last_five_artists()


artist = Artist(name='2-asdfg+++++')
artist.artist_id = 277
artist.save()
print_last_five_artists()


query = Artist.update(name=Artist.name + '!!!').where(Artist.artist_id > 275)
query.execute()
print_last_five_artists()


artist = Artist.get(Artist.artist_id == 279)
artist.delete_instance()
print_last_five_artists()
query = Artist.delete().where(Artist.artist_id > 275)
query.execute()
print_last_five_artists()


conn.close()
