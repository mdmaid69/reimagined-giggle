import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def delete_file(file_name):
        os.remove(file_name)