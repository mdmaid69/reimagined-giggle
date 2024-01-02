import json
print(json.dumps({"name": "John", "age": 30}))
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()