import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time