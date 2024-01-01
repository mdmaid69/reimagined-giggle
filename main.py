def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()