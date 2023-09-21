# AUTHOR EMIL BERGLUND

'''Her er to ulike måter å løse oppgaven med "for-løkke" (selv om det ikke var nødvendig med to)'''
# Jeg tolket fra og med 9 til 101 som at 9 skal telles med, men ikke 101. Da skulle det i såfall stått "til og med 101"
for i in range(9, 101, 2):
    print(i)

for j in range(9, 101):
    if j % 2 != 0:
        print(j)


'''Her er to metoder på hvordan man løser oppgaven med en "while-løkke" (selv om det ikke var nødvendig med to)'''
# Jeg tolket fra og med 9 til 101 som at 9 skal telles med, men ikke 101. Da skulle det i såfall stått "til og med 101"
num = 9
while num <= 101:
    print(num)
    num += 2

y = 9
while y < 101:
    if y % 2!= 0:
        print(y)
    y += 2
