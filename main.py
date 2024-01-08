import os
def change_working_directory(path):
        os.chdir(path)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)