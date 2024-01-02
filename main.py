  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)