import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))