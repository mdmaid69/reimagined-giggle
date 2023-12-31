import json
def read_from_json(json_string):
        return json.loads(json_string)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)