import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_perpetuity(payment, rate):
        return payment / rate