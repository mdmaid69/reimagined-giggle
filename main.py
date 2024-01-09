def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)