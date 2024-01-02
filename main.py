import random
print(random.randint(0, 100))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()