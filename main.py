def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)