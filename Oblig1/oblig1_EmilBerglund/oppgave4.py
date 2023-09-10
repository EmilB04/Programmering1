# AUTHOR EMIL BERGLUND#

a = 6                       #Variabel med navn/str "a" og verdi/int "6"
b = 3                       #Samme som over, men med annet navn og verdi
c = 2                       #Samme som over, men med annet navn og verdi


#Variabler med "oppgave_x" som navn, og formel som verdi
oppgave_a = a + b * c       # 2 * 3 = 6 --> 6 + 6 = 12 | (c * b) + a
oppgave_b = (a + b) * c     # 6 + 3 = 9 --> 9 * 2 = 18 | c * (b + a)
oppgave_c = a / b / c       # 6 / 3 = 2 --> 2 / 2 = 1 | a / b / c
oppgave_d = a / (b / c)     # 3 / 2 = 1.5 --> 6 / 1.5 = 4 | b / c / a

print(f"Oppgave A: {oppgave_a}\nOppgave B: {oppgave_b}\nOppgave C: {oppgave_c}\nOppgave D: {oppgave_d}") #Skriver ut resultatet av variablene med litt pyntetekst og linjseskift