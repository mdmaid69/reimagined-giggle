import json
def convert_to_json(data):
        return json.dumps(data)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)