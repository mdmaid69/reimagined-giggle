import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time