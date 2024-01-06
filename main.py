import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  def calculate_area_triangle(b, h):
        return 0.5 * b * h