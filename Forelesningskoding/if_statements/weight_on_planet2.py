# AUTHOR EMIL BERGLUND #

# liste med planeter 
planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 23.79, 10.44, 8.87, 11.15]
print("---Planeter---")
print("1. Merkur")
print("2. Venus")
print("3. Jorden")
print("4. Mars")
print("5. Jupiter")
print("6. Saturn")
print("7. Uranus")
print("8. Neptun")

planetValg = False
while planetValg == False:
    try:
        planetNummer = int(input("Velg et planetnummer: "))
        if planetNummer > len(planeter):
            print("Velg et gyldig tall")
        elif planetNummer < 0:
            print("Velg et gyldig tall")
        else:
            planetValg = True
            planetNummer = planetNummer - 1
    
    except ValueError:
        print("Skriv et tall fra listen")

print(planetNummer)