import json
def read_from_json(json_string):
        return json.loads(json_string)
import shutil
def delete_directory(path):
        shutil.rmtree(path)