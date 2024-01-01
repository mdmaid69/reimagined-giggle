def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()