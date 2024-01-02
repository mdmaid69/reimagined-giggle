x = 10
y = 20
print("Sum:", x + y)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()