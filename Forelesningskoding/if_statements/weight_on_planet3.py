planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 23.79, 10.44, 8.87, 11.15]

kjør = True
while kjør:
    #introduksjon
    print("\n----------------------------------------")
    print("-- Hva er din vekt på en annen planet --")
    print("----------------------------------------\n")
    
    for planetnummer in range(len(planeter)): # 0-7
        print(f"Planet {planetnummer + 1}: {planeter[planetnummer]}")

# Velg planet
    while True:
        try:
            planetnummer = int(input("Velg planetnummer: "))-1
            print(f"Du har valgt {planeter[planetnummer]}")
            break
        except ValueError:
            print("Du må skrive inn et heltall")
# Skriv inn din vekt på Jorden og få ut din vekt på andre planeter
    while True:
        try:
            din_vekt = float(input("Skriv inn din vekt på Jorden: "))

            jordens_tyngdekraft = tyngdekraft[2]
            din_masse = din_vekt / jordens_tyngdekraft
            din_vekt_på_planet = din_masse * tyngdekraft[planetnummer]
            print(f"Din vekt på {planeter[planetnummer]} er {din_vekt_på_planet:.2f} kg.")
            break
        except ValueError:
            print("Du må skrive inn et tall")
# Spør brukeren vil prøve igjen
    while True:
        try:
            en_gang_til = input("Vil du prøve igjen? (ja/nei): ").lower()
            if en_gang_til == "ja":
                break
            elif en_gang_til == "nei":
                print("Ok")
                kjør = False
                break
            else:
                print("Skriv inn enten ja eller nei")
        except:
            print("Skriv inn enten ja eller nei")