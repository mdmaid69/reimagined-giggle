import json
print(json.dumps({"name": "John", "age": 30}))
import os
def change_working_directory(path):
        os.chdir(path)