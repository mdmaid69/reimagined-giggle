import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)