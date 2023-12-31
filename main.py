import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)