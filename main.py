import json
def convert_to_json(data):
        return json.dumps(data)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()