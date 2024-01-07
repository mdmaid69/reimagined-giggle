import json
def read_from_json(json_string):
        return json.loads(json_string)
def calculate_acceleration(speed, time):
        return speed / time