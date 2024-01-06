import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_perpetuity(payment, rate):
        return payment / rate