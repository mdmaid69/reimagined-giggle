text = "Hello, world!"
print("Words:", len(text.split()))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()