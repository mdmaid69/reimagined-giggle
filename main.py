def reverse_string(s):
        return s[::-1]
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()