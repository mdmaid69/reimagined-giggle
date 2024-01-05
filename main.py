def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)