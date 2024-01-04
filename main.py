import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)