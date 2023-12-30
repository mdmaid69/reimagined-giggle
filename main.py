import json
print(json.dumps({"name": "John", "age": 30}))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()