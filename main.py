import json
def read_from_json(json_string):
        return json.loads(json_string)
import datetime
def get_current_datetime():
        return datetime.datetime.now()