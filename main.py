import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
for i in range(5):
        print(i)