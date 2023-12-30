import json
print(json.dumps({"name": "John", "age": 30}))
import shutil
def move_file(src, dst):
        shutil.move(src, dst)