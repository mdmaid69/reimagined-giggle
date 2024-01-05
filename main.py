import json
def convert_to_json(data):
        return json.dumps(data)
def calculate_perpetuity(payment, rate):
        return payment / rate