def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True