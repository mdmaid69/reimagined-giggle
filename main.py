def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()