import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
text = "Hello, world!"
print("Uppercase:", text.upper())