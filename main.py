def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)