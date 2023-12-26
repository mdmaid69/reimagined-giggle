  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)