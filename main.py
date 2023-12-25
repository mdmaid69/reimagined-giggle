import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])