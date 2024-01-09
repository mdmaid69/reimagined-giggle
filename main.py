import platform
def get_python_version():
        return platform.python_version()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)