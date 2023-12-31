def is_odd(n):
        return n % 2 != 0
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()