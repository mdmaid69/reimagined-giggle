import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2