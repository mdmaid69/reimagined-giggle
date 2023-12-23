import os
def get_environment_variable(var):
        return os.getenv(var)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()