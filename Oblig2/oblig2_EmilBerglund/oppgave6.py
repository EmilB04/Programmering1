# AUTHOR EMIL BERGLUND #

class Format:                   #Til underline
    end = '\033[0m'
    underline = '\033[4m'

pakkeLøkke = True
velg = True
pakkeliste = []
#------------------------------------------------------------------------------------------------
while pakkeLøkke:
    while velg:
        try:
            print("\n",Format.underline,"Velg en av alternativene under ved å skrive ett av tallene:", Format.end)
            brukerValg = int(input("1. Legg til nytt element i pakkelisten \n2. Slett et element fra pakkelisten \n3. Se hele pakkelisten \n4. Avslutt programmet\n: "))
            
#-------------------------------------------------------------------------------------------------
            if brukerValg == 1: # Legg til nytt element i pakkelisten
                print("\n",Format.underline,"Skriv inn elementet du vil legge til i pakkelisten",Format.end)
                element = input(": ")
                pakkeliste.append(element)
                print(f"'{element}' er lagt til i pakkelisten.")
#-------------------------------------------------------------------------------------------------
            elif brukerValg == 2: #Slett et element fra pakkelisten
                if len(pakkeliste) > 0: # Sjekker om listen er tom eller ikke
                    while True:
                        try:
                            print("\n-----------------------")
                            for i in range(1, len(pakkeliste) + 1):
                                element = pakkeliste[i - 1]
                                print(f"{i}. {element}")
                            print("-----------------------")
                            print(Format.underline,"Hvilke element vil du slette? (angi nummer)",Format.end)
                            slettValg = int(input(": "))
                            if (slettValg >= 1) and (slettValg <= len(pakkeliste)):
                                slett_element = pakkeliste.pop(slettValg - 1)
                                print(f"{slett_element} er fjernet fra pakkelisten")
                                break
                            else:
                                print("Ugyldig valg, prøv igjen")
                        except ValueError:
                            print("Du må skriv et tall")
                else:
                    print("Pakkelisten er tom. Det er ingenting å slette.")
#----------------------------------------------------------------
            elif brukerValg == 3: # Se hele pakkelisten
                if len(pakkeliste) > 0:
                    print("\n",Format.underline,"Pakkelisten inneholder følgende elementer:",Format.end)
                    print("-----------------------")
                    for element in pakkeliste:
                        print(element)
                    print("----------------------")
                else:
                    print("Pakkelisten er tom.")
#-----------------------------------------------------------------
            elif brukerValg == 4:
                while True:
                    try:
                        print("\n",Format.underline,"Vil du avslutte programmet? (ja/nei)",Format.end)
                        bekreftelse = input(": ").lower()
                        if bekreftelse == "ja":
                            print("Ok, programmet avsluttes")
                            velg = False
                            pakkeLøkke = False  # Dette vil avslutte den ytre løkken
                            break  # Dette vil avslutte denne indre while-løkken
                        elif bekreftelse == "nei":
                            print("Ok, programmet avsluttes ikke")
                            break
                        else:
                            print("Her skrev du noe feil, skriv enten 'ja' eller 'nei'")
                    except ValueError:
                        print("Her skrev du noe feil")
            else:
                print("Du må skrive et gyldig tall (1, 2, 3 eller 4)")
        except ValueError:
            print("Du må skrive et tall (1, 2, 3 eller 4)")

print("Takk for at du brukte pakkeliste programmet!")
