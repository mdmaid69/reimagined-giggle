import platform
def get_python_version():
        return platform.python_version()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)