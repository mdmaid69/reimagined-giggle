import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)