# AUTHOR EMIL BERGLUND #

student = {
    "fornavn"      : "Ola",
    "etternavn"    : "Nordmann",
    "favorittkurs" : "Programmering 1"}

# 1: Skriv ut studentens fullstendige navn (fornavn og etternavn).
print(student["fornavn"], student["etternavn"])

# 2: Programmatisk endre studentens favorittkurs til å inkludere kursets emnekode: "ITF10219 Programmering 1"
student["favorittkurs"] = "ITF10219 " + student["favorittkurs"]  # Metode 1
# student["favorittkurs"] = "ITF10219 Programmering 1"           # Metode 2
print(student["favorittkurs"])

# 3: Programmatisk legg til en alder for studenten i dictionarien. Du kan selv velge hva alderen skal være.
student["alder"] = 18
print(student["alder"])

#---------------------
print(student)