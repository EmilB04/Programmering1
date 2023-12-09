from datetime import date

car_register = {
    "toyotaBZ4X": {
        "brand": "Toyota",
        "model": "Corolla",
        "price": 96_000,
        "year": 2012,
        "month": 8,
        "new": False,
        "km": 163_000,
    },
    "peugeot408": {
        "brand": "Peugeot",
        "model": "408",
        "price": 330_000,
        "year": 2019,
        "month": 1,
        "new": False,
        "km": 40_000,
    },
    "audiRS3": {
        "brand": "Audi",
        "model": "RS3",
        "price": 473_000,
        "year": 2022,
        "month": 2,
        "new": True,
        "km": 0,
    },
}


def print_car_information(car):
    print(f"Brand: {car['brand']}")
    print(f"Model: {car['model']}")
    print(f"Price: {car['price']}")
    print(f"Manufactured: {car['year']}-{car['month']}")
    print(f"Condition: {'New' if car['new'] == True else 'Used'}")
    print()


def create_car(car_register, brand, model, price, year, month, new, km):
    car = {
        f"{brand}{model}": {
            "brand": brand,
            "model": model,
            "price": price,
            "year": year,
            "month": month,
            "new": new,
            "km": km,
        }
    }
    return car_register.update(car)


def get_car_age(car):
    car_new_year = car["year"]
    today_year = date.today().year
    car_age = today_year - car_new_year
    return car_age


def next_eu_control(car):
    car_new_year = car["year"]
    car_new_month = car["month"]
    next_eu_control_year = car_new_year + 2
    next_eu_control_month = car_new_month
    next_eu_control_day = 1

    next_eu_control_date = (
        f"{next_eu_control_day}.{next_eu_control_month}.{next_eu_control_year}"
    )
    return next_eu_control_date


NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000


def rent_car_monthly_price(car):
    car_price = car["price"]
    if is_new(car):
        car_price += RENT_NEW_CAR__FEE
    yearly_car_price = car_price * 0.4
    monthly_car_price = yearly_car_price / 12 

    final_rent_price = f"{monthly_car_price:.2f}"
    return final_rent_price


def calculate_total_price(car):
    # Oppgave 3.6
    pass


def is_new(car):
    return car["new"]


if __name__ == "__main__":
    create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)

    toyota = car_register["toyotaBZ4X"]
    print_car_information(toyota)
    print(
        f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr."
    )
    print(
        f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}"
    )
    print(
        f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}."
    )

    audi = car_register["audiRS3"]
    print_car_information(audi)
    print(
        f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr."
    )
    print(
        f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}"
    )
    print(
        f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr."
    )
