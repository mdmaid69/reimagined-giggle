  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)