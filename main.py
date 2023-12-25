import os
def list_files_in_directory(path):
        return os.listdir(path)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)