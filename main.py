def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets