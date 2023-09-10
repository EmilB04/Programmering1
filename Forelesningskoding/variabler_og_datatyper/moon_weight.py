# AUTHOR EMIL BERGLUND #
# Vekt på jorda (kilogram)
# my_earth_weight = 75
my_earth_weight = float(input("Vennligst skriv inn din vekt på jorda: "))

# Tyngdekraft på jorda og månen
earth_gravity = 9.807
moon_gravity = 1.622

# Formel for å beregne vekten på månen ut ifra vekten på jorda
moon_weight = (my_earth_weight/earth_gravity) * moon_gravity

# Skriver ut resultatet (min vekt på månen)
# moon_weight = round(moon_weight, 2)
print(f"Din månevekt er {moon_weight:.2f} kg.")