  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)