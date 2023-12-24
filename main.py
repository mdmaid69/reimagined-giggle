import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import glob
def find_files(pattern):
        return glob.glob(pattern)