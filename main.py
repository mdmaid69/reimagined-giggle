import json
def convert_to_json(data):
        return json.dumps(data)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time