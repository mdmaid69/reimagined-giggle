import json
print(json.dumps({"name": "John", "age": 30}))
import os
def remove_directory(path):
        os.rmdir(path)