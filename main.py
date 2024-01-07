import json
def convert_to_json(data):
        return json.dumps(data)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())