import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import json
def read_from_json(json_string):
        return json.loads(json_string)