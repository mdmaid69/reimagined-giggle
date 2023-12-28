def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps