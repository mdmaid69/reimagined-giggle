  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import shutil
def delete_directory(path):
        shutil.rmtree(path)