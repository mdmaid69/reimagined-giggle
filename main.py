  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)