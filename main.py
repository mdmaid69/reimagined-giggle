import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()