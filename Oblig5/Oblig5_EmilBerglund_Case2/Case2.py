from datetime import date

car_register = {
    "toyotaBZ4X": {
        "brand": "Toyota",
        "model": "Corolla",
        "price": 96_000,
        "year": 2012,
        "month": 8,
        "new": False,
        "km": 163_000
    },
    "peugeot408": {
        "brand": "Peugeot",
        "model": "408",
        "price": 330_000,
        "year": 2019,
        "month": 1,
        "new": False,
        "km": 40_000
    },
    "audiRS3": {
        "brand": "Audi",
        "model": "RS3",
        "price": 473_000,
        "year": 2022,
        "month": 2,
        "new": True,
        "km": 0
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
            "km": km
        }
    }
    car_register.update(car)    # Samme som append, bare for dictionaries


def get_car_age(car):
    currentYear = date.today().year
    carYear = car['year']
    yearsOld = currentYear - carYear
    return yearsOld


def next_eu_control(car):
    carYear = car['year']; carMonth = car['month']; carDay = 1
    next_control = carYear + 2
    return f"{next_control}-{carMonth}-{carDay}"

NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000

def rent_car_monthly_price(car):
    carPrice = car['price']
    yearlyCarPrice = carPrice * RENT_CAR_PERCENTAGE
    monthlyCarPrice = yearlyCarPrice / 12
    
    if is_new(car) == True:
        monthlyCarPrice += RENT_NEW_CAR__FEE
    return f"{monthlyCarPrice:.2f}"


def calculate_total_price(car):
    car_age = get_car_age(car)
    car_price = car["price"]

    NEW_CAR_FEE = 8745
    USED_CAR_FEE = {"0-3": 6681, "4-11": 4034, "12-29": 1729, "30+": 0}
    if is_new(car):
        total_price = car_price + NEW_CAR_FEE
        return total_price
    if car_age <= 3 and car_age >= 0:
        total_price = car_price + USED_CAR_FEE["0-3"]
    elif car_age <= 11:
        total_price = car_price + USED_CAR_FEE["4-11"]
    elif car_age <= 29:
        total_price = car_price + USED_CAR_FEE["12-29"]
    else:
        total_price = car_price + USED_CAR_FEE["30+"]
    return total_price


def is_new(car):
    return car['new']


if __name__ == '__main__':
    create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)
    
    print()
    toyota = car_register['toyotaBZ4X']
    print_car_information(toyota)
    print(f"The total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.")
    print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")
    print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}.")
    
    print()
    audi = car_register['audiRS3']
    print_car_information(audi)
    print(f"The total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.")
    print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")
    print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr.")
    
    
# Oppgave 7
    # HER
    
    
class Car:
    def __init__(self, brand, model, price, year, month, new, km):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km

    def print_car_information(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")
        print(f"Manufactured: {self.year}-{self.month}")
        print(f"Condition: {'New' if self.new == True else 'Used'}")
        print()

    def get_car_age(self):
        current_year = date.today().year
        years_old = current_year - self.year
        return years_old

    def next_eu_control(self):
        car_day = 1
        next_control = self.year + 2
        return f"{next_control}-{self.month}-{car_day}"

    def rent_car_monthly_price(self):
        yearly_car_price = self.price * 0.4
        monthly_car_price = yearly_car_price / 12

        if self.is_new():
            monthly_car_price += 1000
        return f"{monthly_car_price:.2f}"

    def calculate_total_price(self):
        new_car_fee = 10783
        used_car_fee = {
            "0-3": 6681,
            "4-11": 4034,
            "12-29": 1729,
            "30+": 0
        }
        if self.is_new():
            total_price = self.price + new_car_fee
        elif self.get_car_age() <= 3:
            total_price = self.price + used_car_fee['0-3']
        elif self.get_car_age() <= 11:
            total_price = self.price + used_car_fee['4-11']
        elif self.get_car_age() <= 29:
            total_price = self.price + used_car_fee['12-29']
        else:
            total_price = self.price + used_car_fee['30+']
        return total_price

    def is_new(self):
        return self.new

print("\n")

toyota = car_register['toyotaBZ4X']
toyota_car = Car(toyota['brand'], toyota['model'], toyota['price'], toyota['year'], toyota['month'], toyota['new'], toyota['km'])
toyota_car.print_car_information()
print(f"The total price for this {toyota_car.brand} {toyota_car.model} is {toyota_car.calculate_total_price()}kr.")
print(f"Next EU-control for the {toyota_car.brand} {toyota_car.model} is {toyota_car.next_eu_control()}")
print(f"If you want to rent the {toyota_car.brand} {toyota_car.model} the monthly fee will be {toyota_car.rent_car_monthly_price()}kr.")