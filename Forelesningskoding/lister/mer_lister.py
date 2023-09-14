zoo_animals = ["Panda", "Lion", "Giraffe", "Alligator"]

# Fjerning av elementer
zoo_animals.pop(0)                      # Må bruke index
zoo_animals.remove("Lion")              # Må bruke str
# Addering av elementer     
zoo_animals.append("Panda")             #Legges til slutten
zoo_animals.insert(3, "Lion")           #Velger index plass og legger til
zoo_animals.insert(3, "Mountain Lion")  #Tar over plassen til "Lion" og dytter den til index 4

print(zoo_animals)