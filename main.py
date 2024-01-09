  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)