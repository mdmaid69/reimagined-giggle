import json
def convert_to_json(data):
        return json.dumps(data)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)