import os
def get_file_size(filename):
        return os.path.getsize(filename)
import json
print(json.dumps({"name": "John", "age": 30}))