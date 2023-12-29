import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import datetime
def get_current_datetime():
        return datetime.datetime.now()