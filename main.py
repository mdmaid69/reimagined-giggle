import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_power(work, time):
        return work / time