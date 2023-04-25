from db.run_sql import run_sql

from models.artists import Artist  
from models.albums import Album
# import repositories.artist_repository as artist_repo 


def save(album):
    sql = f"INSERT INTO album (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album



