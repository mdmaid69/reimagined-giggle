import itertools
print(list(itertools.permutations([1, 2, 3])))
import json
def read_from_json(json_string):
        return json.loads(json_string)