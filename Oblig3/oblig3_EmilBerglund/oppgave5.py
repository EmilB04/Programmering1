# AUTHOR EMIL BERGLUND #



'''Oppgave 5.1'''
#A) Opprett en liste med filmer (hvor hver film er en egen dictionary med dataene om én film). 
#Dataene om en film skal minst være: name, year og rating. Legg til filmene: 
#Inception – 2010 – 8.7 , #Inside Out – 2015 – 8.1 , #Con Air – 1997– 6.9  

filmer = []
filmer.append({"name": "Inception", "year": 2010, "rating": 8.7})
filmer.append({"name": "Inside Out", "year": 2015, "rating": 8.1})
filmer.append({"name": "Con Air", "year": 1997, "rating": 6.9})

# B) Opprett en funksjon som legger til en film i filmlisten. Denne funksjonen skal være definert slik at den minst tar følgende parametere: 
#Listen filmen skal legges til i name year rating 
#Benytt funksjonen til å legge til 3 filmer du selv bestemmer. 

#C) Modifiser funksjonen fra forrige deloppgave til å sette default ratingen 
# til 5.0 hvis det ikke gis noen rating som argument til funksjonen. 
def leggTilFilm(name, year, rating=5.0): 
    nyFilm = {"name": name, "year": year, "rating": rating}
    filmer.append(nyFilm)

leggTilFilm("Spectre", 2014)                        #Siden denne mangler det siste parameteret blir den automatisk 5.0
leggTilFilm("The Shawshank Redemption", 1994, 8.1)  #Siden denne ikke mangler det siste parameteret blir 5.0 overskrevet med lagt til rating
leggTilFilm("The Godfather", 1972, 6.9)



'''Oppgave 5.2'''
#Utvid forrige oppgave med noen funksjoner og benytt dem i koden din. 
#A) Lag en funksjon som printer ut alle filmene i en gitt liste med filmer slik at hver filmutskrift blir seende slik ut: 
#The Lion King - 1994 has a rating of 8.5 

def printFilm(liste):
    for film in liste:
        navn = film["name"]
        år = film["year"]
        rangering = film["rating"]
        print(f"{navn} - {år} har en rating på {rangering}")
printFilm(filmer)

#B) Lag en funksjon som tar en liste med filmer og regner ut 
# gjennomsnittsratingen for alle filmene i lista og returnerer dette. 
# Test funksjonen og skriv ut gjennomsnittet. 

def gjennomSnittRating():
    gjennomsnitt = float(0)
    for film in filmer:
        gjennomsnitt += film["rating"]
    gjennomsnitt /= len(filmer)
    return gjennomsnitt

gjennomsnitt = gjennomSnittRating()
print(f"\nGjennomsnittet er {gjennomsnitt:.2f}\n")

#C) Lag en funksjon som tar en liste med filmer og et årstall som parametere, og returnerer en ny liste med alle filmer fra og med det gitte årstallet. 
#Benytt funksjonen, og print ut informasjon om alle filmer fra og med 2010 (Kan vi  bruke en av funksjonene vi har laget tidligere til å hjelpe oss med noe av dette?). 

def returnerFilmer(liste, årFra, årTil):
    nyFilmer = []
    for film in liste:
        if (film["year"] >= årFra) and (film["year"] <= årTil):
            nyFilmer.append(film)
    printFilm(nyFilmer) # Bruker den tidligere funksjonen til å printe ut relevante filmer
returnerFilmer(filmer, 2010,2014)


'''Oppgave 5.3'''
#A) Opprett en funksjon som tar en liste med filmer, og filnavn som parameter. Benytt denne funksjonen til å skrive alle filmene i lista til en fil du selv velger navnet på f.eks. "movies.txt". Hvis filen allerede eksisterer, skal den overskrives. Legg gjerne til hver film som en egen linje i filen med et fint format. For eksempel: 
#The Lion King - 1994 has a rating of 8.5 

def listeFraFil(liste, filnavn):
    with open(filnavn, "w") as fil: # w = write
        for film in liste:
            fil.write(f"{film['name']} - {film['year']} har en rating på {film['rating']}\n")
listeFraFil(filmer, "movies.txt")

#B) Lag en funksjon som leser den samme filen (filnavn som inputparameter til funksjonen) og skriver ut innholdet til terminalen.
def lesFil(filnavn):
    with open(filnavn, "r") as fil: # r = read
        print("--------------------------------------------")
        for linje in fil:
            print(linje)
        print("--------------------------------------------")
lesFil("movies.txt")
