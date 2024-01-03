import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal