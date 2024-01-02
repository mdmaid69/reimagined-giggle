import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import shutil
def delete_directory(path):
        shutil.rmtree(path)