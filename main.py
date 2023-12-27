import datetime
print(datetime.datetime.now())
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)