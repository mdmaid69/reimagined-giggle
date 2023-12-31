import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)