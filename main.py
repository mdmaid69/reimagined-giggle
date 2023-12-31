import json
def convert_to_json(data):
        return json.dumps(data)
import glob
def find_files(pattern):
        return glob.glob(pattern)