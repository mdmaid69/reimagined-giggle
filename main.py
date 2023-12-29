import glob
def find_files(pattern):
        return glob.glob(pattern)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)