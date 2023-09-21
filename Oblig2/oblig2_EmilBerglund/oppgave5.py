# AUTHOR EMIL BERGLUND #
import random as rd

antall = False
while not antall:
    try:
        antallSpillere = int(input("Hvor mange skal spille dart? "))
        if antallSpillere <= 0:
            print("Det må være minst én spiller")
        else:
            antall = True
    except ValueError:
        print("Du må skrive inn et gyldig tall.")

# Generer antall spillere og scoreboard
spillere = []
scoreBoard = []
for spiller in range(1, antallSpillere + 1):
    spillere.append("Spiller " + str(spiller))
    scoreBoard.append(0)

# Funksjon for kasting av dartpiler.
def kastDart():
    resultat = []  # Lager en liste for resultatene av tre kast
    for i in range(3):
        resultat.append(rd.randrange(0, 60)) # Tolker "mellom 0 og 60" slik jeg har skrevet det. Skal 60 inkluderes er det bare å endre til 61
    return resultat


for i in range(antallSpillere):
    kast_resultater = kastDart()    # Henter poengene fra funksjonen
    for poeng in kast_resultater:   # Går gjennom listen fra funksjonen
        scoreBoard[i] += poeng      # Oppdater poengene til den aktuelle spilleren

for i in range(antallSpillere):
    print(f"{spillere[i]} fikk {scoreBoard[i]} poeng.")
