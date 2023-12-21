import json
def read_from_json(json_string):
        return json.loads(json_string)
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5