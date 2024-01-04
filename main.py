import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)