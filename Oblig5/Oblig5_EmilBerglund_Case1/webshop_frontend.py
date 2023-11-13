# AUTHOR EMIL BERGLUND #

import webshop as ws
from wallet import *

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
        "number_in_stock": 31,
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
ws.add_number_of_ware_to_shopping_cart("hdmi_cable", all_wares["hdmi_cable"], shopping_cart, 2)

# skriver ut handlevognen
print()
print("The shopping cart: ", end="\n")
for ware_key, amount in shopping_cart.items():
    print(f"{all_wares[ware_key]['name']} - {amount} pcs. ")
print(f"\nTotal price of the shopping cart: {ws.calculate_shopping_cart_price(shopping_cart, all_wares, 1.25)} kr.")


# Oppretter en lommebok som inneholder 10000 kr
wallet = Wallet(10000)

# Forsøker å kjøpe varene i handlevognen
ws.buy_shopping_cart(shopping_cart, all_wares, 1.25, wallet)
print()

# Skriver ut mengden penger i lommeboka etter kjøpet
print(f"The amount in the wallet is now {wallet.get_amount()} kr.")