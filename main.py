def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)