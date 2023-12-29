import time
def get_current_time():
        return time.time()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)