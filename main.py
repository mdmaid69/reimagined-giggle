import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)