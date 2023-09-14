# AUTHOR EMIL BERGLUND #

# Gå gjennom listen "tolken_sine_boker" og legg dem til i den tomme listen hvis de er i Lord of the Rings-trilogien. Skriv så ut innholdet i den nye lista ved hjelp av en for -løkke. Det er flere måter man kan skrive en for -løkke på, forsøk å demonstrere et par forskjellige i denne oppgaven.

# Listen er hentet fra Oppgave 3, etter å ha oppdarert den med "Lord of the Rings" forran de som var i trilogien.
tolken_sine_boker = [
    "The Hobbit",
    "Farmer Giles of Ham",
    "Lord of the Rings: The Fellowship of the Ring",
    "Lord of the Rings: The Two Towers",
    "Lord of the Rings: The Return of the King",
    "The Adventures of Tom Bombadil",
    "Tree and Leaf",
]

ny_liste = []

# Metode 1
for bok in tolken_sine_boker:
    if "Lord of the Rings:" in bok:
        ny_liste.append(bok)
    else:
        continue
'''
# Metode 2
for i in range(len(tolken_sine_boker)):
    if "Lord of the Rings:" in tolken_sine_boker[i]:
        ny_liste.append(tolken_sine_boker[i])
    else:
        continue
'''
# Skriver ut de nye elemtene som da er bøkene i Lord of The Rings trilogien, nedover.
for boker in ny_liste:
    print(boker)