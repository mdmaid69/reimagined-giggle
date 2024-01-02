def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)