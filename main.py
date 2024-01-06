def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import json
def read_from_json(json_string):
        return json.loads(json_string)