import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)