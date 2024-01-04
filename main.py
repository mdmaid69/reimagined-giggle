  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import glob
def find_files(pattern):
        return glob.glob(pattern)