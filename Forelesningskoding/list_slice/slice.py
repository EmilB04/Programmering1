#random movies in a list
movies = ["The Matrix", "12 Angry Men", "Pulp Fiction", "Into the Wild", "The Lord of the Rings"]
print(movies[2:])
# Pulp fiction, into the wild, the lord of the rings
print(movies[:2])
# The Matrices, 12 Angry Men
print(movies[2:5])
# Fra og med - til
print(movies[::2])
# Annehvert spill
firstGame = movies[0]
print(firstGame[0:5])
# fem første bokstavene i elementet

copy_of_movies = movies[:]
copy_of_movies[0] = "The Matrix Reloaded"
