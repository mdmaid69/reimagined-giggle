for i in range(10): print(i)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()