import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time