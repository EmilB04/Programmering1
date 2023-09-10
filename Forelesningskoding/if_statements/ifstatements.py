# AUTHOR EMIL BERGLUND # 

'''
number = 0

if (number > 0):
    print(f"{number} er et positivt tall")

elif (number < 0):
    print(f"{number} er et negativt tall")

else: 
    print(f"Tallet er 0")


if ("text" == "Text"):
    print("Venstre side er lik høyre side")
else:
    print("text" == "Text")
'''

dolphins_sleep_with_thei_eyes_open = True
if dolphins_sleep_with_thei_eyes_open == True:
    print(f"Delfiner somver med ett øye åpent")


x = 40
y = 30
er_x_storre_enn_y = y < x
if er_x_storre_enn_y == True:
    print(f"{y} er mindre enn {x}")
#--------------------------------------#
number  = 10

if number > 0:
    print(f"{number} er et positivt tall")

elif number < 0:
    print(f"{number} er et negativt tall")

else: 
    print("Tallet er 0")
#-------------------------------------#
navn = "Emil Berglund"
navn2 = "EmIL bErGlund"

if navn.lower() == navn2.lower():
    print("Navnene er like")