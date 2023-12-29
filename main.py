import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)