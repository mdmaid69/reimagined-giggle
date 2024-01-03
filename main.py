def greet(name):
        print(f"Hello, {name}!")
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()