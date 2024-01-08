import json
def read_from_json(json_string):
        return json.loads(json_string)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)