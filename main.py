import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal