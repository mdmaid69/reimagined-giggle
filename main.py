  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import json
def read_from_json(json_string):
        return json.loads(json_string)