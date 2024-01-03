import json
def read_from_json(json_string):
        return json.loads(json_string)
import glob
def find_files(pattern):
        return glob.glob(pattern)