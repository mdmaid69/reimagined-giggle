import time
def get_current_time():
        return time.ctime()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)