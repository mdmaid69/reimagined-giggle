def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import json
def convert_to_json(data):
        return json.dumps(data)