import json
def read_from_json(json_string):
        return json.loads(json_string)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()