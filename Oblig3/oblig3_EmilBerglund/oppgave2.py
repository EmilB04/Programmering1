# AUTHOR EMIL BERGLUND #
# Definer en funksjon som lager en fin utskrift med et tilfeldig generert tall mellom 0 og 100 
#(husk at du kan benytte random.randrange()). Funksjonen skal ikke ta noen parametere. 
import random as rd

def tilfeldig_tall():
    tilfeldig_generert_tall = rd.randrange(0,100)
    return (f"**********\n*** {tilfeldig_generert_tall} ***\n**********")

for i in range(5):
    print(tilfeldig_tall())
    print("")