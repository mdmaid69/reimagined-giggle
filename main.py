def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True