import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])