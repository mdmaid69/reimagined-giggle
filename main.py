import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)