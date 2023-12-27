import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import sys
def add_to_python_path(path):
        sys.path.append(path)