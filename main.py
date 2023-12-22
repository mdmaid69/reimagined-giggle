import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def reverse_string(s):
        return s[::-1]