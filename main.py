import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_average(lst):
        return sum(lst) / len(lst)