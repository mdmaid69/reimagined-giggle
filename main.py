def count_elements(lst):
        return len(lst)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()