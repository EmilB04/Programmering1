import random as rd


def write_header():
    print("\n------------------------------------------------------------------------------------")
    print("--- This program calculates your weight on different planets in our solar system ---")
    print("------------------------------------------------------------------------------------\n")


def write_planetList(planet_list):
    print("0 : Random planet")
    for planetnumber, planet in enumerate(planet_list):
        print(f"{planetnumber + 1} : {planet}")


def userInput(number):
    planetNumber = input(number)
    index = int(planetNumber) - 1
    return index


def choose_random(planet_list):
    index = rd.randrange(0, len(planet_list))
    chosen_element = planet_list[index]
    return chosen_element


def calculate_weight(your_weight, planet_gravity, earth_gravity):
    calculated_weight = your_weight / earth_gravity * planet_gravity
    return (round(calculated_weight, 1))


def one_more_time():
    answer = input("One more time? (y/n): ").lower()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print("Please enter 'y' for yes or 'n' for no")
        one_more_time()
