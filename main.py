n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()