import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
n = 10
print("Cube numbers:", [x**3 for x in range(n)])