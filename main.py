import os
def get_file_size(filename):
        return os.path.getsize(filename)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)