from .values import *
from .media_types import *

# Movie (id, name, imdb) Slottable!
# Episode (id, number, name, imdb)
# Season (id, number, name, episode list)
# Show (id, name, season list, imdb)
# Series (id, name, movie list)

# Slottable =
# Movie - see above
# Disc =
#   Movie Collection Disc (id, name, movie list)
#   Show Disc (id, show, season, disc num, episode list)
# Saved Spot (id, disc)
# Future Spot (id, name)