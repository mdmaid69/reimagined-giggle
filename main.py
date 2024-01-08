import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)