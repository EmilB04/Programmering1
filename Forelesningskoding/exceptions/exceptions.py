
try:
    tall1 = int(input("Skriv inn et tall: "))
    tall2 = int(input("Skriv inn et tall: "))
    svar = tall1/tall2

except ValueError:
    print("Du må skrive inn et tall!")
except ZeroDivisionError:
    print("Du kan ikke dele på 0!")