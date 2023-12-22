def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import json
def convert_to_json(data):
        return json.dumps(data)