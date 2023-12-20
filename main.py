import json
def convert_to_json(data):
        return json.dumps(data)
def calculate_roi(gain, cost):
        return (gain - cost) / cost