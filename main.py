import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import json
def read_from_json(json_string):
        return json.loads(json_string)