import json
print(json.dumps({"name": "John", "age": 30}))
import os
def get_current_working_directory():
        return os.getcwd()