# AUTHOR EMIL BERGLUND #

pakkeLøkke = True
pakkeliste = []

while pakkeLøkke:
    valgt = False
    while not valgt:
        try:
            print("===========================================================")
            print("Velg en av alternativene under ved å skrive ett av tallene:")
            brukerValg = int(input(
                "1. Legg til nytt element i pakkelisten \n2. Slett et element fra pakkelisten \n3. Se hele pakkelisten \n4. Avslutt programmet\n-----------------------------------------------------------\n"))

            if brukerValg == 1: # Legg til nytt element i pakkelisten
                element = input("Skriv inn elementet du vil legge til: ")
                pakkeliste.append(element)
                print(f"{element} er lagt til i pakkelisten.")
#-------------------------------------------------------------------------------------------------
            elif brukerValg == 2:
                while True:
                    if len(pakkeliste) > 0:
                        print("===========================================================")
                        print("Pakkelisten inneholder følgende elementer:")
                        for i, element in enumerate(pakkeliste, 1):
                            print(f"{i}. {element}")
                        print("-------------------------------------------")
                        slett_valg = input("Velg elementet du vil slette (angi nummer) eller skriv 'a' for å gå tilbake til hovedmenyen: ")
                        if slett_valg.lower() == 'a':
                            break
                        try:
                            slett_valg = int(slett_valg)
                            if slett_valg >= 1 and slett_valg <= len(pakkeliste):
                                slett_element = pakkeliste.pop(slett_valg - 1)
                                print(f"{slett_element} er fjernet fra pakkelisten.")
                            else:
                                print("Ugyldig valg. Prøv igjen.")
                        except ValueError:
                            print("Du må skrive et tall eller 'a' for å gå tilbake til hovedmenyen.")
                    else:
                        print("Pakkelisten er tom. Ingenting å slette.")

#----------------------------------------------------------------
            elif brukerValg == 3: # Se hele pakkelisten
                if len(pakkeliste) > 0:
                    print("==========================================")
                    print("Pakkelisten inneholder følgende elementer:")
                    for element in pakkeliste:
                        print(element)
                    print("------------------------------------------")
                else:
                    print("Pakkelisten er tom.")
#-----------------------------------------------------------------
            elif brukerValg == 4:
                while True:
                    try:
                        print("===========================================================")
                        bekreftelse = input("Vil du avslutte programmet (ja/nei): ").lower()
                        if bekreftelse == "ja":
                            print("Ok, programmet avsluttes")
                            pakkeLøkke = False  # Dette vil avslutte den ytre løkken
                            break  # Dette vil avslutte denne indre while-løkken
                        elif bekreftelse == "nei":
                            print("Ok, programmet avsluttes ikke")
                        else:
                            print("Her skrev du noe feil, skriv enten 'ja' eller 'nei'")
                    except ValueError:
                        print("Her skrev du noe feil")
            else:
                print("Du må skrive et gyldig tall (1, 2, 3 eller 4)")
        except ValueError:
            print("Du må skrive et tall (1, 2, 3 eller 4)")

print("Takk for at du brukte pakkeliste-programmet!")
