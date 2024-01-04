  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import json
def convert_to_json(data):
        return json.dumps(data)