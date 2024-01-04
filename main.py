def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import json
def read_from_json(json_string):
        return json.loads(json_string)