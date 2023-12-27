def calculate_area_circle(r):
        return 3.14 * r**2
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()