import itertools
print(list(itertools.permutations([1, 2, 3])))
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)