# AUTHOR EMIL BERGLUND #

#Definer en funksjon som heter print_list(). 
#Denne funksjonen skal ta i mot en liste som parameter, 
#og printe ut hvert element i denne listen en etter en. 
#Lag deretter kort liste med dine 3 favorittmatretter, 
#og kall funksjonen din med denne listen som parameter.

def print_list(liste):
    for element in liste:
        print(element)

mine_favoritretter = ["Biffsnadder", "Taco", "Pizza"]
print_list(mine_favoritretter)