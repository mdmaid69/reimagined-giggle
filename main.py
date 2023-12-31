import json
def read_from_json(json_string):
        return json.loads(json_string)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))