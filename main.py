import time
def get_time_since_epoch():
        return time.time()
import json
def read_from_json(json_string):
        return json.loads(json_string)