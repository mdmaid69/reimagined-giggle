import shutil
def delete_directory(path):
        shutil.rmtree(path)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)