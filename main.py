import json
def read_from_json(json_string):
        return json.loads(json_string)
import time
def get_current_time():
        return time.ctime()