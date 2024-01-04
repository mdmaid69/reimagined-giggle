  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import os
def remove_directory(path):
        os.rmdir(path)