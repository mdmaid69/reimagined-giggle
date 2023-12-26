import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def reverse_string(s):
        return s[::-1]