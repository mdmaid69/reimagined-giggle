import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())