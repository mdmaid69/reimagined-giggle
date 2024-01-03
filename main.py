import json
def read_from_json(json_string):
        return json.loads(json_string)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()