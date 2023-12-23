import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import datetime
def get_current_datetime():
        return datetime.datetime.now()