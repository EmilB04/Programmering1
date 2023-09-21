# AUTHOR EMIL BERGLUND #

ultimate_answer_loop=True
while ultimate_answer_loop:
    try:
        tall=int(input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall: "))
        if tall == 42:
            print("Det stemmer, meningen med livet er 42!")
            ultimate_answer_loop = False
        elif tall < 50 and tall > 30:
            print("Nærme, men feil.")
        else:
            print("FEIL!")
    except ValueError:
        print("Her leste du ikke hintet ser jeg... prøv igjen!")