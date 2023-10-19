import json_modul

planet = {"name" : "Mercury", "gravity" : 3.73}

file_name = "planet.json"
json_modul.write_json(planet, file_name)

dictionary_from_file = json_modul.read_json(file_name)
print(dictionary_from_file)

print(dictionary_from_file["name"])