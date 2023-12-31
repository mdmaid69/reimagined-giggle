  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import shutil
def delete_directory(path):
        shutil.rmtree(path)