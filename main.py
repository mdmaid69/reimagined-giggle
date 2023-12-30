import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import json
def convert_to_json(data):
        return json.dumps(data)