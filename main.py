import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps