import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))