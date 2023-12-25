import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()