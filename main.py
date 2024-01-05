import sys
def add_to_python_path(path):
        sys.path.append(path)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)