import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import json
def read_from_json(json_string):
        return json.loads(json_string)