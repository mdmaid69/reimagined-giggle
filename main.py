  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()