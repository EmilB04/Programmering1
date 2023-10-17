import json

planeter = [{"navn": "Merkur", "Tyngdekraft": 3.7},
            {"navn": "Venus", "Tyngdekraft": 8.87},
            {"navn": "Jorda", "Tyngdekraft": 9.81},            
            ]

with open ("forelesningskoding/fil_lesing_skriving/json/planeter.json", "w") as utfil:
    json.dump(planeter, utfil, indent=4)

with open("forelesningskoding/fil_lesing_skriving/json/planeter.json", "r") as fil:
    planeter_fra_fil = json.load(fil)
    print(planeter_fra_fil)

json_string = '''{
    "dyr" : "Hund",
    "navn" : "Fido",
    "alder" : 5,
    }    
'''
print(json_string)
hund = json.loads(json_string)
print(f"Hunden {hund['navn']} er {hund['alder']} år gammel")