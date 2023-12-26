import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)