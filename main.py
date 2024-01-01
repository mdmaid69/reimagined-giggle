  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()