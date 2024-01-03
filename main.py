import time
def get_current_time():
        return time.time()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)