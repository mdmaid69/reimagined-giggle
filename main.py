import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import json
def convert_to_json(data):
        return json.dumps(data)