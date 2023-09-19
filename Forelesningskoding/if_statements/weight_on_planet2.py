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
        if planetNummer > len(planeter) or planetNummer <= 0:
            print("Velg et gyldig tall")
        else:
            planetNummer = planetNummer - 1
            print(f"Du valgte planet: {planeter[planetNummer]}")
            planetValg = True
    
    except ValueError:
        print("Skriv et tall fra listen")

vekt = False
while vekt == False:
    try:
        din_vekt = int(input("Hva er din vekt på jorden i hele kg? "))
        if din_vekt >= 600:
            print("Du lyver!")
        elif din_vekt <= 0:
            print("Prøv igjen, du veier ikke 'ingenting' kg!")
        else:
            din_masse = din_vekt / tyngdekraft[2]
            tyngdekraftNummer = planetNummer
            vekt_pa_planet = din_masse * tyngdekraft[tyngdekraftNummer]
            print(f"Din vekt på {planeter[planetNummer]} er {vekt_pa_planet:.2f} kg")
            vekt = True  # Hvis input er vellykket, avslutt løkken

    except ValueError:
        print("Du må skrive inn et heltall.")
