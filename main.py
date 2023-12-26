text = "Hello, world!"
print("Reversed:", text[::-1])
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()