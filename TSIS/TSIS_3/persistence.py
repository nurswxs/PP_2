import json   # module for working with JSON

def load_data(file, default):
    # loads data from a JSON file
    # if the file is missing or there is a read error, it returns the default value.
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return default

def save_data(file, data):
    # saves data to a JSON file with indents for easy reading
    with open(file, "w") as f:
        json.dump(data, f, indent=4)