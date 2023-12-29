import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import json
print(json.dumps({"name": "John", "age": 30}))