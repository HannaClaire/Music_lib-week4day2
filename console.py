
from models.albums import Album
from models.artists import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# album_repository.delete_all()
# artist_repository.delete_all()

artist1 = Artist("Jon Hopkins")
artist_repository.save(artist1)
artist2 = Artist("Rura")
artist_repository.save(artist2)

# artist_repository.select_all()

album1 = Album("Singularity", "electronic", "Jon Hopkins")
album_repository.save(album1)

# album2 = Album("Dusk Moon", "Scottish/Folk")
# album_repository.save(album2)
