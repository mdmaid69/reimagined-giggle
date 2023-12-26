import sys
def add_to_python_path(path):
        sys.path.append(path)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)