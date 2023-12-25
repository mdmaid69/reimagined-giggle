n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()