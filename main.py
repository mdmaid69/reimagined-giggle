def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import json
def convert_to_json(data):
        return json.dumps(data)