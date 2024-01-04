  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)