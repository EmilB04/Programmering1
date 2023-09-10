# AUTHOR EMIL BERGLUND#

tall1 = int(input("Vennligst skriv inn ett heltall: "))    # Ber brukeren om å skrive inn et heltall. Her kan kan eventuelt legge inn en loop for hvis brukeren ikke skriver inn et heltall
tall2 = int(input("Vennligst skriv inn ett heltall: "))    # Gjenta linjen over

"""
Tupler med operatortype og hva som skal gjøres (verdi). Man kunne også skrevet dette utenom en liste slik: "gange" = tall1*tall2
Ved å bruke denne formen istedenfor flere variabler, er det lettere å skrive ut senere ved hjelp av en "for løkke".
"""
operatorer = [                                             # Lager en liste med alle operatorene, som gjør det lettere å gå gjennom senere.
    ("Gange", tall1 * tall2),                              
    ("Dele", tall1 / tall2),
    ("Pluss", tall1 + tall2),
    ("Minus", tall1 - tall2),
    ("Modulo", tall1 % tall2),
    ("Opphøye", tall1 ** tall2),
    ("Dele nedrunding", tall1 // tall2)
]

for operator, formel in operatorer:               #Gå gjennom "operatorer"-listen og henter ut "operator" som da blir "gange", "dele" osv. i tillegg til formelen: tall1*tall2 osv.
    print(f"{operator} = {formel}")               #Skriver ut det som blir gått gjennom i for løkken, i terminalen.
