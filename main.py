def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)