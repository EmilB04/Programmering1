
with open ("Forelesningskoding/filLesning/zen_of_python.txt", "r") as fil:
    innhold = fil.read()
    print(innhold)
    print(type(innhold))

with open ("Forelesningskoding/filLesning/zen_of_python.txt", "r") as nyFil:
    linjeListe = nyFil.readlines() # Leser linje for linje
    print(linjeListe)
    print(type(linjeListe))

filnavn = "Forelesningskoding/filLesning/zen_of_python.txt"

with open (filnavn, "r") as fil:
    print(f"\n{fil.readline()} - Første Linje")