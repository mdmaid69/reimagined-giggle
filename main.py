import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import glob
def find_files(pattern):
        return glob.glob(pattern)