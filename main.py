def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)