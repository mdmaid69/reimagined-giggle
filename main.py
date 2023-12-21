def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()