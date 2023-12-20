import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)