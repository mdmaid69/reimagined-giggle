def calculate_density(mass, volume):
        return mass / volume
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()