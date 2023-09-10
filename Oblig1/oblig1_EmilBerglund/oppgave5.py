# AUTHOR EMIL BERGLUND

#Ukesoversikt på fem personer
ukesoversikt = [
    ("person_1", 5 ),
    ("person_2", 9 ),
    ("person_3", 2.5 ),
    ("person_4", 21 ),
    ("person_5", 0 ),
]

antall_småkaker = 0                     #Lager en variabel på antall småkaker, som senere skal øke.
antall_personer = len(ukesoversikt)     #Lager en variabel for å få oversikt over antall personer, som senere skal brukes til gjennomsnitt.

for person, småkaker in ukesoversikt:   #Går gjennom ukesoversikten og ser etter person og småkaker, hvor den adderer småkakene for-løkka finner til "antall_småkaker"
    antall_småkaker += småkaker         #En teller for å få oversikt over antall småkaker.

gjennomsnitt_småkaker = antall_småkaker // antall_personer      #Regner ut gjennomsnittet ved bruk at variablene som ble opprettet tidligere
print(f"Gjennomsnittlig småkaker per person: {int(gjennomsnitt_småkaker)}")                             #Skriver ut gjennomsnittet