import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)