def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)