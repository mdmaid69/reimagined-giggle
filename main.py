numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()