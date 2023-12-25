def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import json
def read_from_json(json_string):
        return json.loads(json_string)