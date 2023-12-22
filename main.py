  import os
  def get_base_name(path):
        return os.path.basename(path)
import json
def convert_to_json(data):
        return json.dumps(data)