  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()