import os
def remove_directory(path):
        os.rmdir(path)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)