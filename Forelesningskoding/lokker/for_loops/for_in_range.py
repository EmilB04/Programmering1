#for tall in range(11): #0-10
#    print(tall)

#for tall in range(1,10,1): #1-9
#    print(tall)

#for tall in range(1000, 9002, 1): #1000-9001
#    print(tall)

nummere = []

for tall in range(1, 20 ,1):
    nummere.append(tall)

for tall in nummere:
    print(tall)

print(min(nummere))     # Laveste tall i listen
print(max(nummere))     # Høyeste tall i listen