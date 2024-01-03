import shutil
def delete_directory(path):
        shutil.rmtree(path)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)