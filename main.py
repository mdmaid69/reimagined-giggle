import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import platform
def get_os_info():
        return platform.uname()