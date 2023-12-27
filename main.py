import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)