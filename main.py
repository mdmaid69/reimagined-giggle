import json
def read_from_json(json_string):
        return json.loads(json_string)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)