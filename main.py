import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)