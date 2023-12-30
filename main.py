import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)