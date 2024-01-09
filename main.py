def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)