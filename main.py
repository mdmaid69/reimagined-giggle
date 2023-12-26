print([x**2 for x in range(10)])
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)