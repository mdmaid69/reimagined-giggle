import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import datetime
def get_current_datetime():
        return datetime.datetime.now()