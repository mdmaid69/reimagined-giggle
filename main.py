def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()