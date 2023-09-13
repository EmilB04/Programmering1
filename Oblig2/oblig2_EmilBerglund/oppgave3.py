# AUTHOR EMIL BERGLUND #

tolken_sine_boker = [
    "The Hobbit", 
    "Farmer Giles of Ham",
    "The Fellowship of the Ring", 
    "The Two Towers",             
    "The Return of the King",     
    "The Adventures of Tom Bombadil",  
    "Tree and Leaf",              
]

#1: Skriv ut de to første og de to siste bøkene i listen.
print(tolken_sine_boker[0])
print(tolken_sine_boker[1])
print(tolken_sine_boker[-2])
print(tolken_sine_boker[-1])

#2: Legg til to av bøkene som ble utgitt etter hans død:
# = alternative måter
tolken_sine_boker.append("The Silmarillion")
#tolken_sine_boker[7] = "The Silmarillion"
tolken_sine_boker.append("Unfinished Tales")
#tolken_sine_boker[8] = "Unfinished Tales")

#3. Gjør endringer på de tre bøkene i Lord of the Rings trilogien og legg til "Lord of the Rings: " foran hver av dem. (hvis dere ikke vet hvilke dette er, vet Google) 
tolken_sine_boker[2] = "Lord of the Rings: " + tolken_sine_boker[2]
tolken_sine_boker[3] = "Lord of the Rings: " + tolken_sine_boker[3]
tolken_sine_boker[4] = "Lord of the Rings: " + tolken_sine_boker[4]

#4. Sorter lista og skriv den ut. 
print("---------------------------------")
tolken_sine_boker.sort() # Sortert i alfabetisk rekkefølge
for boker in tolken_sine_boker:
    print(boker)
print("---------------------------------")