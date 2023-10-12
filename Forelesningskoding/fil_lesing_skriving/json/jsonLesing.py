import json

planeter = [{"navn": "Merkur", "Tyngdekraft": 3.7},
            {"navn": "Venus", "Tyngdekraft": 8.87},
            {"navn": "Jorda", "Tyngdekraft": 9.81},            
            ]

with open ("forelesningskoding/fil_lesing_skriving/json/planeter.json", "w") as utfil:
    json.dump(planeter, utfil, indent=4)
