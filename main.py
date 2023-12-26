import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def convert_to_binary(n):
        return bin(n)