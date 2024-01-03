import json
print(json.dumps({"name": "John", "age": 30}))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)