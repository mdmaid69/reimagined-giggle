from collections import Counter
print(Counter("hello world"))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()