import sys
def print_python_version():
        return sys.version
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()