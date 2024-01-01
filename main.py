def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()