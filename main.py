  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)