import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)