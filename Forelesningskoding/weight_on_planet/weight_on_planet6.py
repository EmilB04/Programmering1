# Skrevet på engelsk
from planet_functions import *
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
gravity = [3.7, 8.87, 9.807, 3.721, 23.79, 10.44, 8.87, 11.15]

# --------------------------------------------------------------------------------------------------------- #
run = True
while run:
    write_header()
    write_planetList(planets)
    planetNumber = userInput("\nChoose planet number: ")

    if planetNumber == -1:
        planet = choose_random(planets)
        print(f"  You got {planet}")
    else:
        planet = planets[planetNumber]
        print(f"  You chose {planet}")

    userWeight = float(input("Insert your weight on Earth in kg: "))
    weight_on_other_planet = calculate_weight(userWeight, gravity[planetNumber], earth_gravity=9.801)
    print(f"  Your weight on {planet} is {weight_on_other_planet} kg.")

    if one_more_time() == False:
        run = False
        print("Ok, bye!")
    else:
        print("Ok, Here we go!")
        continue