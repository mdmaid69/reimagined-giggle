import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))