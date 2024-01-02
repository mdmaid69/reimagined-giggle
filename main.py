  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)