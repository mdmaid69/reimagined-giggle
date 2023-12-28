import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)