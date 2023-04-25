from db.run_sql import run_sql

from models.albums import Album  # ADDED
from models.artists import Artist
import repositories.album_repository as album_repo


def save(artist):
    sql = f"INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


# , artist.artist.id
