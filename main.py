import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import time
def get_time_since_epoch():
        return time.time()