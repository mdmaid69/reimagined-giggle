import json
print(json.dumps({"name": "John", "age": 30}))
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)