import os
def change_working_directory(path):
        os.chdir(path)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()