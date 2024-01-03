import time
def get_time_since_epoch():
        return time.time()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)