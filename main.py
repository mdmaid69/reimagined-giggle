import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)