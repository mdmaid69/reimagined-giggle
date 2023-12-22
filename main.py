import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
n = 10
print("Powers of 2:", [2**x for x in range(n)])