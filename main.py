import glob
def find_files(pattern):
        return glob.glob(pattern)
import json
print(json.dumps({"name": "John", "age": 30}))