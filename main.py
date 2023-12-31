import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)