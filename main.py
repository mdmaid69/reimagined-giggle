import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)