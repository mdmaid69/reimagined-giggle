def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import json
def read_from_json(json_string):
        return json.loads(json_string)