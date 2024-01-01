import json
def convert_to_json(data):
        return json.dumps(data)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time