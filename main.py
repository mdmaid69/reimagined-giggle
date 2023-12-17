import json
def convert_to_json(data):
        return json.dumps(data)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time