import json
print(json.dumps({"name": "John", "age": 30}))
import shutil
def delete_directory(path):
        shutil.rmtree(path)