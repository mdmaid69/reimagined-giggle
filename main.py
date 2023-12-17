import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue