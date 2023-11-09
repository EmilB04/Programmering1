#------------------------------------------
#Oppgaver
#------------------------------------------

def print_ware_information(ware):
    '''Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.'''
    print(f"\nName: {ware['name']}")
    print(f"Price: {ware['price']}")
    print(f"Number in stock: {ware['number_in_stock']}")
    print(f"Description: {ware['description']}")

def calculate_average_ware_rating(ware):
    ''''Returnerer den gjennomsnittlige ratingen for en spesifisert vare.'''
    ratings = ware['ratings']
    total_rating = 0
    
    for rating in ratings:
        total_rating += rating
        try:
            average_rating = total_rating / len(ratings)
        except ZeroDivisionError:
            average_rating = 0
    return f"{float(average_rating):.1f}"

def get_all_wares_in_stock(all_wares):
    '''Returnerer en dictionary med alle varer som er på lager.'''
    '''Den returnerte dictionarien skal følge samme format som vareregisteret i webshop_frontent.py (all_wares-variabelen).'''
    all_wares_in_stock = {}
    for ware_key, ware_item in all_wares.items():
        if is_ware_in_stock(ware_item):
            all_wares_in_stock[ware_key] = ware_item
            
    return all_wares_in_stock

def is_number_of_ware_in_stock(ware, number_of_ware):
    '''Returnerer en Boolean-verdi som representerer om et spesifisert antall foav
    en gitt vare finnes på lager.'''
    if ware['number_in_stock'] >= number_of_ware:
        return True     # På lager
    else:
        return False    # Ikke på lager

def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):
    '''Legger til et spesifisert antall av en gitt vare i en spesifisert handlevogn.'''
    if is_number_of_ware_in_stock(ware, number_of_ware):
        shopping_cart[ware_key] = number_of_ware    # Legger til vare i handlevogn
        ware['number_in_stock'] -= number_of_ware   # Oppdaterer antall varer på lager
    else:
        print(f"ERROR: The number of {ware['name']} in stock is less than {number_of_ware}.")

def calculate_shopping_cart_price(shopping_cart, all_wares, tax):
    '''Returnerer prisen av en handlevogn basert på varene i den.'''
    shopping_cart_price = 0
    for ware_key, number_of_ware in shopping_cart.items():
        shopping_cart_price += all_wares[ware_key]['price'] * number_of_ware
    shopping_cart_price *= tax
    return shopping_cart_price

def can_afford_shopping_cart(shopping_cart_price, wallet):
    '''Returnerer en Boolean-verdi basert på om det er nok penger i en gitt lommebok for å kjøpe en handlevogn.'''
    if shopping_cart_price <= wallet.get_amount():
        return True     # Har råd
    else:
        return False    # Har ikke råd


# Prøv å få til denne
def buy_shopping_cart(shopping_cart, all_wares, tax, wallet):
    # Kjøper varene i en handlevogn. Parameterene defineres i oppgaven.
    shopping_cart_value = calculate_shopping_cart_price(shopping_cart, all_wares, tax)
    # Finn totalprisen av handlevognen og trekk fra i wallet.
    total_subtraction = wallet.get_amount() - shopping_cart_value
    # Oppdaterer lommeboken
    wallet.subtract_amount(total_subtraction)
    # Tømmer handlevognen etter kjøp
    clear_shopping_cart(shopping_cart)

#------------------------------------------
# Predefinerte funksjoner
#------------------------------------------

def is_ware_in_stock(ware):
    '''Returnerer en Boolean-verdi som representerer om en vare er på lager.'''
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False

def clear_shopping_cart(shopping_cart):
    '''Tømmer en handlevogn.'''
    shopping_cart.clear()
