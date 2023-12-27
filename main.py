  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import os
def get_file_size(filename):
        return os.path.getsize(filename)