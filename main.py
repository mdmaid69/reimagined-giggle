import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import platform
def get_os_info():
        return platform.uname()