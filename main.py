import platform
def get_os_info():
        return platform.uname()
import json
print(json.dumps({"name": "John", "age": 30}))