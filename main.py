  import os
  def get_base_name(path):
        return os.path.basename(path)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)