import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)