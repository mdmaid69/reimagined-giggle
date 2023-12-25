import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)