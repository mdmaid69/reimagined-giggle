import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b