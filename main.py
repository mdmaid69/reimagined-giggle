  import sys
  def get_python_version():
        return sys.version
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)