import os
print(os.getcwd())
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()