import random as rd

def skriv_hei():
    print("-------------")
    print("---- Hei ----")
    print("-------------")

skriv_hei()
#----------------------------------------------------------------

def gi_tilfeldig_tall(tall1, tall2):
    tilfeldig_tall = rd.randrange(tall1,tall2)
    print(tilfeldig_tall)
gi_tilfeldig_tall(1,10)