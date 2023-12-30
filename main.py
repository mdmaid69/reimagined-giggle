import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)