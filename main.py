import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import json
def convert_to_json(data):
        return json.dumps(data)