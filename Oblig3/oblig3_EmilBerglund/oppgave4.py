# AUTHOR EMIL BERGLUND #

"""Lag en funksjon for å regne ut volumet av et tredimensjonelt objekt. 
Vi lar ting være enkelt og forholder oss bare til enkle verdier 
for lengde, bredde og høyde. Volumet kan da beregnes med følgende formel: 
lengde*bredde*høyde. Du skal ta lengden, bredden og høyden som individuelle 
inputparametere for funksjonen, og returnere volumet. 
Kall funksjonen noen ganger med forskjellige verdier for 
lengde, bredde og høyde, og skriv ut resultatet av hver utregning.
"""

def beregn_volum(lengde, bredde, høyde):
    volum = lengde * bredde * høyde
    print(f"Volumet er {volum:.2f} m3")

beregn_volum(2, 5, 10)
beregn_volum(1, 3, 2.5)
beregn_volum(1, 1, 2)

#eller 

while True:
    try:
        lengde = float(input("Lengde: "))
        bredde = float(input("Bredde: "))
        høyde = float(input("Høyde: "))
        break
    except ValueError:
        print("Du må skrive inn et tall")
        continue

beregn_volum(lengde, bredde, høyde)