import platform
def get_os_info():
        return platform.uname()
import json
def read_from_json(json_string):
        return json.loads(json_string)