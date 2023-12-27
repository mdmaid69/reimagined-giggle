def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)