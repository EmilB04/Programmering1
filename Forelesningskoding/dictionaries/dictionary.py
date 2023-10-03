movies = {
    "tittel" : "Dixit",
    "spilletid" : 30,
    "aldersgrense" : 8
}

print(movies)
print()

print(movies["spilletid"])
print()

movies["spilletid"] = 40
print(movies)
print(movies.get('spilletid'))

movies["beskrivelse"] = "Give the perfect clue so most (not all) players guess the right surreal image card"
print(movies)

movies.pop("beskrivelse")
del movies["spilletid"]
print(movies)

for key in movies.keys():
    print(key)
print()
for value in movies.values():
    print(value)
print()
for key, value in movies.items():
    print(key, value)


brettspill = [
    {"tittel" : "Dixit", "spilletid" : 30, "aldersgrense" : 8, "år" : 2008},
    {"tittel" : "Pandemic" , "spilletid" : 45, "aldersgrense" : 8, "år" : 2008},
    {"tittel" : "Wingspan", "spilletid" : 60, "aldersgrense" : 8, "år" : 1977}
]

for spill in brettspill:
    print(f"{spill['tittel']} er ment for spillere fra {spill['aldersgrense']} år og oppover")

brettspill.append({"tittel" : "Myserium", "spilletid" : 40, "aldersgrense" : 10})
