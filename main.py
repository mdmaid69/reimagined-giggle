import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import platform
def get_os_info():
        return platform.uname()