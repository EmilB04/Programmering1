# AUTHOR EMIL BERGLUND #


'''Oppgave 5.1'''
#A) Opprett en liste med filmer (hvor hver film er en egen dictionary med dataene om én film). Dataene om en film skal minst være: name, year og rating. Legg til filmene: 
#Inception – 2010 – 8.7 
#Inside Out – 2015 – 8.1 
#Con Air – 1997– 6.9  

filmer = []
filmer.append({"name": "Inception", "year": 2010, "rating": 8.7})
filmer.append({"name": "Inside Out", "year": 2015, "rating": 8.1})
filmer.append({"name": "Con Air", "year": 1997, "rating": 6.9})

#--------------------------------------------------------------------------
# B) Opprett en funksjon som legger til en film i filmlisten. Denne funksjonen skal være definert slik at den minst tar følgende parametere: 
#Listen filmen skal legges til i name year rating 
#Benytt funksjonen til å legge til 3 filmer du selv bestemmer. 

#C) Modifiser funksjonen fra forrige deloppgave til å sette default ratingen 
# til 5.0 hvis det ikke gis noen rating som argument til funksjonen. 
# Test at dette fungerer ved å legge til en film uten å spesifisere dens rating. 
def leggTilFilm(name, year, rating=5.0): 
    nyFilm = {"name": name, "year": year, "rating": rating}
    filmer.append(nyFilm)

leggTilFilm("Spectre", 2014)                        #Siden denne mangler det siste parameteret blir den automatisk 5.0
leggTilFilm("The Shawshank Redemption", 1994, 8.1)  #Siden denne ikke mangler det siste parameteret blir 5.0 overskrevet med lagt til rating
leggTilFilm("The Godfather", 1972, 6.9)

#for film in filmer:
    #print(film)

'''Oppgave 5.2'''
#Utvid forrige oppgave med noen funksjoner og benytt dem i koden din. 
#A) Lag en funksjon som printer ut alle filmene i en gitt liste med filmer slik at hver filmutskrift blir seende slik ut: 

def printFilm():
    for film in filmer:
        print(film["name"],"-", film["year"],"has a rating of", film["rating"])


printFilm()