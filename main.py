import json
print(json.dumps({"name": "John", "age": 30}))
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)