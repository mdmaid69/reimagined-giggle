text = "Hello, world!"
print("Uppercase:", text.upper())
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()