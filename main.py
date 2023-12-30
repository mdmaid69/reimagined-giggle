import datetime
print(datetime.datetime.now())
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)