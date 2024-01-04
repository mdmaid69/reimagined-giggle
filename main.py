numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()