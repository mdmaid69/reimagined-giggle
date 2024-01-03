  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)