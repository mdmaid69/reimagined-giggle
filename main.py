def find_max(numbers):
        return max(numbers)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()