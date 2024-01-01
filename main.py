import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time