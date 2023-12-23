import platform
def get_python_version():
        return platform.python_version()
import json
def convert_to_json(data):
        return json.dumps(data)