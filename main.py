def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()