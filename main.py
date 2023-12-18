import json
def convert_to_json(data):
        return json.dumps(data)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)