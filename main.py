import json
def convert_to_json(data):
        return json.dumps(data)
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare