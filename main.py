import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)