import json
print(json.dumps({"name": "John", "age": 30}))
import os
def list_files_in_directory(path):
        return os.listdir(path)