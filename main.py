import sys
print(sys.version)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()