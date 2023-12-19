  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)