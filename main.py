import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
print([x**2 for x in range(10)])