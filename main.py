  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)