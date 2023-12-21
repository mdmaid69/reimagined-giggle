i = 0
while i < 5:
        print(i)
        i += 1
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()