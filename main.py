import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]