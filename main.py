import json
print(json.dumps({"name": "John", "age": 30}))
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)