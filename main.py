import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)