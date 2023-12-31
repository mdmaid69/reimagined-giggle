def calculate_pressure(force, area):
        return force / area
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()