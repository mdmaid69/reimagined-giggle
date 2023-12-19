import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_speed(distance, time):
        return distance / time