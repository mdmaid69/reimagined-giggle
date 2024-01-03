def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()