def calculate_roi(gain, cost):
        return (gain - cost) / cost
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()