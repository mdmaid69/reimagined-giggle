import datetime
print(datetime.datetime.now())
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)