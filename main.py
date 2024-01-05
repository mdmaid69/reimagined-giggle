import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets