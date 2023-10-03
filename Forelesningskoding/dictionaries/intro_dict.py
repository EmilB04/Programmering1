movies = {"tittel": "The Shawshank Redemption", "kategori": "Romance", "score": 9.99, "pris": 19.99}

print(movies["tittel"])
print(movies.get("tittel"))

del movies["pris"]
#movies.pop("pris")
print(movies)