# ------------------------------------------
# Oppgaver
# ------------------------------------------
def print_ware_information(ware):
    '''Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.'''

def calculate_average_ware_rating(ware):
    ''''Returnerer den gjennomsnittlige ratingen for en spesifisert vare.'''

def get_all_wares_in_stock(all_wares):
    '''Returnerer en dictionary med alle varer som er på lager.'''

def is_number_of_ware_in_stock(ware, number_of_ware):
    '''Returnerer en Boolean-verdi som representerer om et spesifisert antall av
    en gitt vare finnes på lager.'''

def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware):
    '''Legger til et spesifisert antall av en gitt vare i en spesifisert
    handlevogn.'''

def calculate_shopping_cart_price(shopping_cart, all_wares, tax):
    '''Returnerer prisen av en handlevogn basert på varene i den.'''

def can_afford_shopping_cart(shopping_cart_price, wallet):
    '''Returnerer en Boolean-verdi basert på om det er nok penger i en gitt
    lommebok for å kjøpe en handlevogn.'''

def buy_shopping_cart():
    '''Kjøper varene i en handlevogn. Parameterene defineres i oppgaven.'''

# ------------------------------------------
# Predefinerte funksjoner
# ------------------------------------------
def is_ware_in_stock(ware):
    '''Returnerer en Boolean-verdi som representerer om en vare er på lager.'''
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False

def clear_shopping_cart(shopping_cart):
    '''Tømmer en handlevogn.'''
    shopping_cart.clear()

# FILEPATH: /C:/Users/emilb/OneDrive/Dokumenter/HIOF/H_2023/Programmering1/Oblig5/wallet.py

class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def subtract_amount(self, value):
        self.amount -= value

# FILEPATH: /C:/Users/emilb/OneDrive/Dokumenter/HIOF/H_2023/Programmering1/Oblig5/webshop_frontend.py

import webshop as ws
from wallet import Wallet

all_wares = {
    "amd_processor": {
        "name": "AMD Ryzen 9 5900X Processor",
        "price": 5590.0,
        "number_in_stock": 50,
        "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
        "description": "All the cores and threads you'll need!",
    },
    "playstation_5": {
        "name": "PlayStation 5",
        "price": 5999.0,
        "number_in_stock": 0,
        "ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
        "description": "Next generation console, never in stock!",
    },
    "hdmi_cable": {
        "name": "Belkin Ultra High Speed HDMI Cable - 2m",
        "price": 349.0,
        "number_in_stock": 3,
        "ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0],
        "description": "A high speed overprices HDMI cable!",
    }
}

# Filtrer ut alle varer som er på lager og skriv ut informasjonen for hver av dem
all_wares_in_stock = ws.get_all_wares_in_stock(all_wares)
for ware in all_wares_in_stock.values():
    ws.print_ware_information(ware)

# Skriv ut den gjennomsnittlige ratingen for denne varen
print(f"Average rating for the AMD Processor: {ws.calculate_average_ware_rating(all_wares['amd_processor'])}")
print()

# Oppretter en tom handlevogn
shopping_cart = {}

# Forsøker å legge til 1 amd processor, 2 playstation 5 konsoller og 3 hdmi kabler
ws.add_number_of_ware_to_shopping_cart("amd_processor", all_wares["amd_processor"], shopping_cart)
ws.add_number_of_ware_to_shopping_cart("playstation_5", all_wares["playstation_5"], shopping_cart, 2)
ws.add_number_of_ware_to_shopping_cart("hdmi_cable", all_wares["hdmi_cable"], shopping_cart, 4)

# skriver ut handlevognen
print()
print(f"The shopping cart: {shopping_cart}")
print()

# Oppretter en lommebok som inneholder 10000 kr
wallet = Wallet(10000)

# Forsøker å kjøpe varene i handlevognen
ws.buy_shopping_cart('''Parameterne blir definert i oppgaven''')
print()

# Skriver ut mengden penger i lommeboka etter kjøpet
print(f"The amount in the wallet after the purchase: {wallet.get_amount()}")

# FILEPATH: /C:/Users/emilb/OneDrive/Dokumenter/HIOF/H_2023/Programmering1/Oblig5/webshop.py

def print_ware_information(ware):
    '''Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.'''
    print(f"Name: {ware['name']}")
    print(f"Price: {ware['price']} NOK")
    print(f"Number in stock: {ware['number_in_stock']}")
    print(f"Description: {ware['description']}")

def calculate_average_ware_rating(ware):
    ''''Returnerer den gjennomsnittlige ratingen for en spesifisert vare.'''
    return sum(ware["ratings"]) / len(ware["ratings"])

def get_all_wares_in_stock(all_wares):
    '''Returnerer en dictionary med alle varer som er på lager.'''
    return {key: value for key, value in all_wares.items() if is_ware_in_stock(value)}

def is_number_of_ware_in_stock(ware, number_of_ware):
    '''Returnerer en Boolean-verdi som representerer om et spesifisert antall av
    en gitt vare finnes på lager.'''
    return ware["number_in_stock"] >= number_of_ware

def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):
    '''Legger til et spesifisert antall av en gitt vare i en spesifisert
    handlevogn.'''
    if is_number_of_ware_in_stock(ware, number_of_ware):
        shopping_cart[ware_key] = shopping_cart.get(ware_key, 0) + number_of_ware
        ware["number_in_stock"] -= number_of_ware
        print(f"{number_of_ware} instance(s) of {ware['name']} were added to the shopping cart.")
    else:
        print(f"{ware['name']} is not in stock and could not be added to the shopping cart.")

def calculate_shopping_cart_price(shopping_cart, all_wares, tax):
    '''Returnerer prisen av en handlevogn basert på varene i den.'''
    total_price = 0
    for ware_key, number_of_ware in shopping_cart.items():
        total_price += all_wares[ware_key]["price"] * number_of_ware
    total_price *= (1 + tax)
    return total_price

def can_afford_shopping_cart(shopping_cart_price, wallet):
    '''Returnerer en Boolean-verdi basert på om det er nok penger i en gitt
    lommebok for å kjøpe en handlevogn.'''
    return wallet.get_amount() >= shopping_cart_price

def buy_shopping_cart(shopping_cart, all_wares, wallet, tax=0.25):
    '''Kjøper varene i en handlevogn.'''
    shopping_cart_price = calculate_shopping_cart_price(shopping_cart, all_wares, tax)
    if can_afford_shopping_cart(shopping_cart_price, wallet):
        for ware_key, number_of_ware in shopping_cart.items():
            all_wares[ware_key]["number_in_stock"] += number_of_ware
        wallet.subtract_amount(shopping_cart_price)
        print(f"The total price will be {shopping_cart_price:.2f}")
        print("Transaction finished. Wares bought:")
        print(shopping_cart)
    else:
        print("Transaction failed. Not enough money in wallet.")
