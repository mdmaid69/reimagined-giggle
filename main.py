import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)