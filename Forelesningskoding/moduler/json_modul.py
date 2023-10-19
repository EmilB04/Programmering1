import json

def write_json(dictionary, file_name):
    try:
        with open(file_name, "w") as file:
            json.dump(dictionary, file, indent=4)

    except FileNotFoundError:
        print("We couldn't find the file. Please try again.")

def read_json(file_name):
    try:
        with open(file_name, "r") as file:
            dictionary_from_file = json.load(file)
    
    except FileNotFoundError:
        print("We couldn't find the file. Please try again.")
    except json.decoder.JSONDecodeError:
        print("The file is empty. Please try again.")
    else:
        return dictionary_from_file
