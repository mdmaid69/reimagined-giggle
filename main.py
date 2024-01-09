import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import datetime
def get_current_date():
        return datetime.date.today()