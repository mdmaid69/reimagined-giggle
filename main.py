import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)