import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)