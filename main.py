import json
def convert_to_json(data):
        return json.dumps(data)
import shutil
def delete_directory(path):
        shutil.rmtree(path)