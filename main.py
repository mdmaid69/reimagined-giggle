def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)