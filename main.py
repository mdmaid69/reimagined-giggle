import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)