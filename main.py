import time
print(time.time())
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()