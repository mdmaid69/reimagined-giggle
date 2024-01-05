  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)