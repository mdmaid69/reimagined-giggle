import time
def get_time_since_epoch():
        return time.time()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)