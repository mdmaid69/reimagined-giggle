import platform
def get_python_version():
        return platform.python_version()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)