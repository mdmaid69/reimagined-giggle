import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets