import json
def convert_to_json(data):
        return json.dumps(data)
import platform
def get_os_info():
        return platform.uname()