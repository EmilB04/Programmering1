
with open ("Forelesningskoding/filLesning/zen_of_python.txt", "r") as fil:
    innhold = fil.read()
    print(innhold)

with open ("Forelesningskoding/filLesning/zen_of_python.txt", "r") as nyFil:
    linjeListe = nyFil.readlines() # Leser linje for linje
    print(linjeListe)