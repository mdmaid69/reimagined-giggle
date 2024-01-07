import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r