import json
print(json.dumps({"name": "John", "age": 30}))
import platform
def get_os_info():
        return platform.uname()