import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)