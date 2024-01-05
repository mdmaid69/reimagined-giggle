import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time