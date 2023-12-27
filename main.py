  import os
  def delete_file(file_name):
        os.remove(file_name)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)