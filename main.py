def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)