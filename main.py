def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)