import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)