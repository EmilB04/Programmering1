# AUTHOR EMIL BERGLUND #
'''Hva er din vekt på andre planeter'''

vekt = True
while vekt:
    try:
        din_vekt = int(input("Hva er din vekt på jorden i hele kg? "))
        if din_vekt >= 600:
            print("Du lyver!")
        elif din_vekt <= 0:
            print("Prøv igjen, du veier ikke ingenting kg!")
        else:
            vekt = False  # Hvis input er vellykket, avslutt løkken
    except ValueError:
        print("Du må skrive inn et heltall.")

planeter = True
while planeter:
    planeter_i_melkeveien = [
    "merkur", "venus", "jorden",
    "jorda", "mars", "jupiter",
    "saturn", "uranus", "neptun",
]
    planetNavn = input("Hva er planetens navn? ").lower()
    if planetNavn == "pluto":
        print("Pluto er ikke en planet, din donut!")
    elif planetNavn.isnumeric():
        print("Skriv inn et planetnavn, ikke et tall!")
    elif planetNavn not in planeter_i_melkeveien:
        print("Skriv inn en planet som faktisk finnes, daahh!")
    else:
        print("OK")
        planeter = False

tyngdekraft = True
while tyngdekraft:
    try:
        planetens_tyngdekraft = float(input("Hva er planetes tyngdekraft? "))
        if planetens_tyngdekraft <=0:
            print(f"Tyngdekraften {planetens_tyngdekraft} kan ikke være 0 eller lavere")
        else:
            print("OK")
            tyngdekraft = False
    except ValueError:
        print("Skriv inn tall, ikke bokstaver")

jordens_tyngdekraft = 9.81
din_masse = din_vekt / jordens_tyngdekraft
din_planetVekt = din_masse * planetens_tyngdekraft

print(f"Selv om du veier {din_vekt}kg på jorda, veier du {din_planetVekt:.0f}kg på {planetNavn} med en tyngdekraft på {planetens_tyngdekraft}")