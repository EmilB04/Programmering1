teller = 10
while teller > 0:
    print(teller)
    teller -= 1
            
while teller < 11:
    print(teller)
    teller += 11

liste_m_tall = []
for tall in range(7):
    liste_m_tall.append(tall)
    print(liste_m_tall)

while 3 in liste_m_tall:
    liste_m_tall.pop()
    print(liste_m_tall)

avslutt = False
while not avslutt:
    print("Test")
    for nummer in range(2):
        print(nummer)
    en_gang_til = input("Skriv ut en gang til (Y/N)").upper()
    if en_gang_til == "Y":
        avslutter = True
        break
    else:
        pass