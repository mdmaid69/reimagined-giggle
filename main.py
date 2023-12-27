  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)