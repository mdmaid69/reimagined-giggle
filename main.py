def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True