import json
def read_from_json(json_string):
        return json.loads(json_string)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)