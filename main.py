import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets