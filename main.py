import sys
def add_to_python_path(path):
        sys.path.append(path)
import json
print(json.dumps({"name": "John", "age": 30}))