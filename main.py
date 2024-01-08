import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))