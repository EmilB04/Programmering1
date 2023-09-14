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


# Generer antall spillere
spillere = []
for spiller in range(1, antallSpillere+1):
    spillere.append("Spiller " + str(spiller))
print(spillere)

# Hver person skal kaste 3 ganger hver
scoreListe = [[] for _ in range(antallSpillere)] # forenkle dette

for spiller_index in range(antallSpillere):
    for kast in range(3):
        score = rd.randrange(0, 60)
        scoreListe[spiller_index].append(score)

print(scoreListe)