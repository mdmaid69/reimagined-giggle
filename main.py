import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time